import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import pickle
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

from preTrained import get_state

# Parameters
lr = 0.005
episodes = 1000
tb_writer = tf.summary.create_file_writer(f"./runs/{time.time()}")

# Loading pre-trained model 
with open("cartpoleQ.pkl", "rb") as f:
    Q = pickle.load(f)

# Parsing the givenn sketch
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

# Initializing environment
env = gym.make("CartPole-v0")

# Optimizing the program
optimiser = tf.keras.optimizers.Adam(learning_rate=lr)

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
			inputData = {
				"h1": observation[0],
				"h2": observation[1],
				"h3": observation[2],
				"h4": observation[3],
			}

			# Target model value
			label = Q[get_state(observation)].argmax()	    
		
			# Adding to loss
			CodegenFns.g = g
			train_fn = TFCodegen(tree.get_node(tree.root), tree)
			val = callGraph(train_fn, inputData)
			loss += (label-val)**2
			
			# Selecting an action
			action = env.action_space.sample()

			# Next frame please
			observation, reward, done, _ = env.step(label)

			batch_size += 1

		loss /= batch_size

	sources = [item[1] for item in trainable_map.items()]
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
	    inputData = {
	    	"h1": obs[0],
	    	"h2": obs[1],
	    	"h3": obs[2],
	    	"h4": obs[3],
	    }
	    train_fn = TFCodegen(tree.get_node(tree.root), tree)
	    action = callGraph(train_fn, inputData)
	    action = action.numpy().round().astype(int)[0]
	    obs, reward, done, _ = env.step(action)
	    cum_reward += reward

	print("Cumulative Reward of the program:", cum_reward)
	with tb_writer.as_default():
		tf.summary.scalar("Cumulative Reward", cum_reward, ep)


print("Final generated variables:", trainable_map)
