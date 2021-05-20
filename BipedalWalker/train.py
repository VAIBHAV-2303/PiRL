from collections import namedtuple
import os
from typing import List
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import torch
import tensorflow as tf
import gym 
import time
import numpy as np

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

from pretrained.ddpg_agent import Agent

def getInput(obs):
	inputData = {
		"h0": obs[0],
		"h1": obs[1],
		"h2": obs[2],
		"h3": obs[3],
		"h4": obs[4],
		"h5": obs[5],
		"h6": obs[6],
		"h7": obs[7],
		"h8": obs[8],
		"h9": obs[9],
		"h10": obs[10],
		"h11": obs[11],
		"h12": obs[12],
		"h13": obs[13],
	}
	return inputData

# Parameters
lr = 0.005
episodes = 1000
batch_size = 32
buffer_size = 10000
num_samples = 50

tb_writer = tf.summary.create_file_writer(f"./runs/{time.time()}")

# Creating environment
env = gym.make('BipedalWalker-v3')

# Loading pre-trained model
state_dim = env.observation_space.shape[0]
action_dim = env.action_space.shape[0]
agent = Agent(state_size=state_dim, action_size=action_dim, random_seed=0)
agent.actor_local.load_state_dict(torch.load('pretrained/checkpoint_actor.pth', map_location="cpu"))
agent.critic_local.load_state_dict(torch.load('pretrained/checkpoint_critic.pth', map_location="cpu"))
agent.actor_target.load_state_dict(torch.load('pretrained/checkpoint_actor.pth', map_location="cpu"))
agent.critic_target.load_state_dict(torch.load('pretrained/checkpoint_critic.pth', map_location="cpu"))

# Parsing the given sketch
lexer = MetaGrammarLexer.MetaGrammarLexer(StdinStream())
token_stream = CommonTokenStream(lexer)
parser = MetaGrammarParser(token_stream)
tree = parser.sketch()
tree.accept(SketchBuilderVisitor())

# Generating a random program from the sketch
tree = getProgTree(rule_table.start, 5)
print("=================Generated Program==============")
for leaf in tree.leaves():
    print(leaf.data.name, end=' ')
print()

# Optimizing the program
optimiser = tf.keras.optimizers.Adam(learning_rate=lr)
train_fn = TFCodegen(tree.get_node(tree.root), tree)

class Buffer:
	ObservationType = namedtuple('ObservationType', 'obs, oracle_action')

	def __init__(self, size = 1000) -> None:
		self.size = 1000
		self.buffer = []

	def remove(self):
		remove_idx = int(np.random.choice(np.arange(0, len(self.buffer)), size=(1,)))
		self.buffer.pop(remove_idx)

	def add(self, obs, oracle_action):
		if len(self.buffer) == self.size:
			self.remove()

		self.buffer.append(Buffer.ObservationType(obs, oracle_action))


	def sample(self, batch_size):
		batch_size = min(batch_size, len(self.buffer))
		probs = 1/np.arange(1, len(self.buffer)+1)
		probs /= probs.sum()
		idxs = np.arange(0, len(self.buffer))
		chosen_idxs = np.random.choice(idxs, size=(batch_size, ), replace=False, p = probs)

		chosen_samples = [self.buffer[idx] for idx in chosen_idxs]
		return chosen_samples

def genHistory(oracle, agent, buffer : Buffer):
	observation = env.reset()
	done = False
	while not done:
		inputData = getInput(observation)
		oracle_action = oracle.act(observation, False)
		buffer.add(observation, oracle_action)
		
		agent_action = callGraph(agent, inputData)
		observation, reward, done, _ = env.step(agent_action)	
	


buffer = Buffer(buffer_size)
# Training
it = 0

for ep in range(episodes):
	
	genHistory(agent, train_fn, buffer)

	for _ in range(num_samples):
		batch = buffer.sample(batch_size = batch_size)
		loss = 0

		with tf.GradientTape() as g:
			for sample in batch:
				inputData = getInput(sample.obs)
				agent_action = callGraph(train_fn, inputData)
				oracle_action = sample.oracle_action

				loss += tf.reduce_sum((agent_action - tf.constant(oracle_action))**2)
		
			loss /= len(batch)

		sources = trainable_map
		grads = g.gradient(loss, sources)

		optimiser.apply_gradients(zip(grads, sources))

		print("Episode:", it, "Loss:", loss)
		with tb_writer.as_default():
			tf.summary.scalar("loss", loss, it)
		
		it += 1

	# Resetting stuff
	# observation = env.reset()
	# done = False
	# loss = 0

	# with tf.GradientTape() as g:
	# 	batch_size = 0
	# 	while not done:
	# 		# env.render()
	# 		inputData = getInput(observation)

	# 		# Target model value
	# 		label = agent.act(observation, 0)[0] # 0 is just noise
	# 		label = tf.constant(label)

	# 		# Adding to loss
	# 		CodegenFns.g = g
	# 		val = callGraph(train_fn, inputData)
	# 		loss += tf.reduce_sum(label-val)**2

	# 		# Next frame please
	# 		observation, reward, done, _ = env.step(val)

	# 		batch_size += 1

		# loss /= batch_size


	# Calculating the reward for the current program
	obs = env.reset()
	done = False
	cum_reward = 0
	while not done:
	    inputData = getInput(obs)
	    action = callGraph(train_fn, inputData)
	    obs, reward, done, _ = env.step(action)
	    cum_reward += reward

	print("Cumulative Reward of the program:", cum_reward)
	with tb_writer.as_default():
		tf.summary.scalar("Cumulative Reward", cum_reward, it)


print("Final generated variables:", trainable_map)
