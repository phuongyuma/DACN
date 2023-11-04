import gym
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from networkEnv import NetworkEnv
from function import DeepQLearning

nums_samples = 3
nums_traffic_analyzer = 3
# traffic_flow_distribution = 0.8

env = NetworkEnv(num_samples=nums_samples, num_traffic_analyzer=nums_traffic_analyzer)

gamma=1
epsilon=0.1
numberEpisodes= 13 #1000

# create an object
LearningQDeep=DeepQLearning(env,gamma,epsilon,numberEpisodes, num_samples=nums_samples, num_traffic_analyzer=nums_traffic_analyzer)
# run the learning process
LearningQDeep.trainingEpisodes(num_samples=nums_samples, num_traffic_analyzer=nums_traffic_analyzer)
# get the obtained rewards in every episode
LearningQDeep.sumRewardsEpisode

#  summarize the model
LearningQDeep.mainNetwork.summary()
LearningQDeep.mainNetwork.save("dqn_trained_model_temp.h5")