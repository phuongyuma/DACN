## env for network in paper "Deep Reinforcement Learning with Double Q-learning"
import gym
from gym import spaces
from gym.spaces import Box, Tuple
import numpy as np
import random

class RoundedBox(Box):
    def __init__(self, low, high, shape, dtype=np.float32):
        super().__init__(low, high, shape=shape, dtype=dtype)
    
    def sample(self):
        # Lấy một mẫu ngẫu nhiên từ action space
        sample = super().sample()
        # Làm tròn giá trị về 2 chữ số sau dấu thập phân
        return np.round(sample, 2)
    
class NetworkEnv(gym.Env):
    # def __init__(self, state_resource, state_Traffic_Analyzer, num_samples, traffic_flow_distribution):
    #     self.state_Traffic_Analyzer = state_Traffic_Analyzer
    #     self.state_resource = state_resource
    #     self.num_samples = num_samples
    #     self.state = np.zeros(self.num_samples, 2)
    def __init__(self, num_samples, num_traffic_analyzer):
        super(NetworkEnv, self).__init__()
        self.state_space = Box(low=0, high=num_traffic_analyzer, shape=(num_samples, 2), dtype=np.float32)
        action_space_1 = gym.spaces.Discrete(num_samples) # determines the sampling points pj ∈ O
        action_space_2 = gym.spaces.Discrete(num_traffic_analyzer) # determines which traffic analyzer to assign at each sampling point
        #action_space_3 = Box(low=-1.0, high=1.0, shape=(1,)) # determines the reduction of the sampling rate
        action_space_3 = RoundedBox(low=-1.0, high=1.0, shape=(1,))
        print("Action space 3 sample: ", action_space_3.sample())
        self.action_space = Tuple([action_space_1, action_space_2, action_space_3])
        self.state = self.reset(num_samples=num_samples, num_traffic_analyzer=num_traffic_analyzer)

    def reset(self, num_samples, num_traffic_analyzer):
        self.state = np.zeros((num_samples, 2))
        return self.state

    def step(self, action):
        print("Action: ", action)
        done = False
        actionA, actionB, actionC = action  # Unpack the 'action' into 'actionA', 'actionB', and 'actionC'
        if not self._is_valid_action(actionA, actionB, actionC):
            raise ValueError("Invalid action provided.")
                
        reward = 1.0 # skip calculate reward temporary 
        actionC = round(actionC, 2)
        # Update the state (fake)
        self.state[actionA, 0] = actionB
        self.state[actionA, 1] = actionC
        print("State: ", self.state)
        return self.state, reward, done
    
    def _is_valid_action(self, actionA, actionB, actionC):
        return (0 <= actionA <= self.state.shape[0] and
                0 <= actionB <= self.state.shape[1] and
                -1.0 <= actionC <= 1.0)
        

