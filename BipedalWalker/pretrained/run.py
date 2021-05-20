from ddpg_agent import Agent
import gym
import torch

# Creating environment
env = gym.make('BipedalWalker-v3')

# Loading pretrained agent
state_dim = env.observation_space.shape[0]
action_dim = env.action_space.shape[0]
agent = Agent(state_size=state_dim, action_size=action_dim, random_seed=0)
agent.actor_local.load_state_dict(torch.load('checkpoint_actor.pth', map_location="cpu"))
agent.critic_local.load_state_dict(torch.load('checkpoint_critic.pth', map_location="cpu"))
agent.actor_target.load_state_dict(torch.load('checkpoint_actor.pth', map_location="cpu"))
agent.critic_target.load_state_dict(torch.load('checkpoint_critic.pth', map_location="cpu"))

# Playing
observation = env.reset()
done = False
cum_reward = 0
while not done:
	env.render()
	action = agent.act(observation, 0)
	observation, reward, done, info = env.step(action[0])
	cum_reward += reward
print("Cumulative Reward:", cum_reward)
env.close()
