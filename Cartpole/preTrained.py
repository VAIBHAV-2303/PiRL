import numpy as np
import gym
from functools import partial

def discretize_val(val, min_val, max_val, num_states):
	"""
	Discretizes a single float
	if val < min_val, it gets a discrete value of 0
	if val >= max_val, it gets a discrete value of num_states-1
	
	Args:
	    val (float): value to discretize
	    min_val (float): lower bound of discretization
	    max_val (float): upper bound of discretization
	    num_states (int): number of discrete states
	
	Returns:
	    float: discrete value
	"""
	state = int(num_states * (val - min_val) / (max_val - min_val))
	if state >= num_states:
		state = num_states - 1
	if state < 0:
		state = 0
	return state

def obs_to_state(num_states, lower_bounds, upper_bounds, obs):
	"""
	Turns an observation in R^N, into a discrete state
	
	Args:
	    num_states (list): list of number of states for each dimension of observation
	    lower_bounds (list): list of lowerbounds for discretization
	    upper_bounds (list): list of upperbounds for discretization
	    obs (list): observation in R^N to discretize
	
	Returns:
	    int: discrete state
	"""
	state_idx = []
	for ob, lower, upper, num in zip(obs, lower_bounds, upper_bounds, num_states):
		state_idx.append(discretize_val(ob, lower, upper, num))

	return np.ravel_multi_index(state_idx, num_states)

env = gym.make('CartPole-v0')
num_actions = env.action_space.n
num_states = [1, 8, 8, 8]
lower_bounds = [-4.8, -3, -0.418, -2]
upper_bounds = [4.8, 3, 0.418, 2]

get_state = partial(obs_to_state, num_states, lower_bounds, upper_bounds)
