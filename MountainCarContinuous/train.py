import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import pickle
import torch
import tensorflow as tf
import gym 
import time

from PiRL import rule_table
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.StdinStream import StdinStream

from PiRL.GrammarParser import MetaGrammarLexer
from PiRL.GrammarParser.MetaGrammarParser import MetaGrammarParser
from PiRL.ProgramGen.ParseTreeGenerator import getProgTree

from PiRL.TFCodegen.TFCodegen import TFCodegen
from PiRL.ProgramGen.SketchBuilderVisitor import SketchBuilderVisitor
from PiRL.TFCodegen.CodegenFns import trainable_map, input_map
from PiRL.TFCodegen import CodegenFns
from PiRL.TFCodegen.TFCodegen import callGraph

from preTrained import Oracle

def getInput(obs):
	inputData = {
		"h0": obs[0],
		"h1": obs[1],
	}
	return inputData

# Parameters
lr = 0.1
episodes = 100
tb_writer = tf.summary.create_file_writer(f"./runs/{time.time()}")

# Creating environment
env = gym.make('MountainCarContinuous-v0')

# Loading pre-trained model
oracle = Oracle()

# Parsing the given sketch
lexer = MetaGrammarLexer.MetaGrammarLexer(StdinStream())
token_stream = CommonTokenStream(lexer)
parser = MetaGrammarParser(token_stream)
tree = parser.sketch()
tree.accept(SketchBuilderVisitor())

# Generating a random program from the sketch
tree = getProgTree(rule_table.start, 20)
print("=================Generated Program==============")
for leaf in tree.leaves():
    print(leaf.data.name, end=' ')
print()

# Optimizing the program
optimiser = tf.keras.optimizers.Adam(learning_rate=lr)
train_fn = TFCodegen(tree.get_node(tree.root), tree)

# Training
for ep in range(episodes):
	
	# Resetting stuff
	observation = env.reset()
	done = False
	loss = 0

	with tf.GradientTape() as g:
		batch_size = 0
		while not done:
			# env.render()
			inputData = getInput(observation)

			# Target model value
			label = oracle.getAction(observation)

			# Adding to loss
			CodegenFns.g = g
			val = callGraph(train_fn, inputData)
			loss += (label-val)**2

			# Next frame please
			observation, reward, done, _ = env.step(label)

			batch_size += 1

		loss /= batch_size

	sources = trainable_map
	grads = g.gradient(loss, sources)
	optimiser.apply_gradients(zip(grads, sources))

	print("Episode:", ep, "Loss:", loss)
	with tb_writer.as_default():
		tf.summary.scalar("loss", loss[0], ep)

	# Calculating the reward for the current program
	obs = env.reset()
	done = False
	cum_reward = 0
	while not done:
	    if ep % 10 == 0:
		    env.render()
	    inputData = getInput(obs)
	    action = callGraph(train_fn, inputData)
	    obs, reward, done, _ = env.step(action)
	    cum_reward += reward

	print("Cumulative Reward of the program:", cum_reward)
	with tb_writer.as_default():
		tf.summary.scalar("Cumulative Reward", cum_reward, ep)


print("Final generated variables:", trainable_map)
