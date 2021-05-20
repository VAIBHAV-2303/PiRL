import gym 

env = gym.make("CartPole-v0")

obs = env.reset()
done = False
cum_reward = 0
while not done:
    env.render()

    if 0.116*obs[0]-0.686*obs[1]-1.158*obs[2]-1.434*obs[3] > -0.345:
    	action = 0 
    else: 
    	action = 1

    obs, reward, done, _ = env.step(action)
    cum_reward += reward

print("Cumulative Reward:", cum_reward)