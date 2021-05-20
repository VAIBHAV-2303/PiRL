import gym 

env = gym.make("MountainCarContinuous-v0")

obs = env.reset()
done = False
cum_reward = 0
while not done:
	env.render()	

	if obs[1] > 0:
		action = 0.7 
	else: 
		action = -0.7 

	obs, reward, done, _ = env.step([action])
	cum_reward += reward

print("Cumulative Reward:", cum_reward)