import gym
import os
import random
import numpy as np
from statistics import mean

class Oracle:

    def __init__(self):
        self.Q = np.load("pretrained.npy")
        self.velocity_obs = [i / 100 for i in range(-7, 8, 1)]
        self.pos_obs = [i / 10 for i in range(-12, 7, 1)]
        self.acts = [i / 10 for i in range(-10, 11, 1)]  # sampling of the action space

    def get_Q_index(self, state):
        for i in range(len(self.pos_obs)):
            # Position
            if self.pos_obs[i] <= state[0] < self.pos_obs[i + 1]:
                # Velocity
                for j in range(len(self.velocity_obs)):
                    if self.velocity_obs[j] <= state[1] < self.velocity_obs[j + 1]:
                        return len(self.velocity_obs) * i + j  # row we need in Q

    def getAction(self, obs):
        state = self.get_Q_index(obs)
        return [self.acts[np.argmax(self.Q[state])]]


if __name__ == '__main__':

    # Loading environment
    env = gym.make('MountainCarContinuous-v0')

    # Loading pre-trained model
    oracle = Oracle()

    # Preview
    obs = env.reset()
    cum_reward = 0
    done = False
    while not done:
        env.render()
        action = oracle.getAction(obs)
        obs, reward, done, _ = env.step(action)
        cum_reward += reward
    print("Cumulative Reward:", cum_reward)
    env.close()
