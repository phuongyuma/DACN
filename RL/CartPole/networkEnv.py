## env for network in paper "Deep Reinforcement Learning with Double Q-learning"
import gym
from gym import spaces
from gym.spaces import Box
import numpy as np
import random



class NetworkEnv(gym.env):
    # def __init__(self, state_resource, state_Traffic_Analyzer, num_samples, traffic_flow_distribution):
    #     self.state_Traffic_Analyzer = state_Traffic_Analyzer
    #     self.state_resource = state_resource
    #     self.num_samples = num_samples

    #     self.state = np.zeros(self.num_samples, 2)
    def __init__(self):
        super(NetworkEnv, self).__init__()
        self.state_space = Box(shape=(3, 2), dtype=int)
        self.action_space = spaces.Discrete(3)  
        self.state = self.reset()


    def reset(self):
        self.state = np.zeros(self.num_samples, 2)
        return self.state

    def step(self, action):
        reward = 0
        done = False
        

