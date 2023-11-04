import keras
from function import DeepQLearning
import gym
import numpy as np
loaded_model = keras.models.load_model("dqn_trained_model.h5",custom_objects={'class_name': DeepQLearning,'my_loss_fn':DeepQLearning.my_loss_fn})

sumObtainedRewards=0

# create the environment, here you need to keep render_mode='rgb_array' since otherwise it will not generate the movie
env = gym.make("CartPole-v1",render_mode='rgb_array')
# reset the environment
(currentState,prob)=env.reset()

video_length=400
# the step_trigger parameter is set to 1 in order to ensure that we record the video every step
#env = gym.wrappers.RecordVideo(env, 'stored_video',step_trigger = lambda x: x == 1, video_length=video_length)
#env = gym.wrappers.RecordVideo(env, 'stored_video', video_length=video_length)
env = gym.wrappers.RecordVideo(env, 'stored_video', step_trigger=lambda x: x == 10  , video_length=video_length)


# since the initial state is not a terminal state, set this flag to false
terminalState=False
while not terminalState:
    # get the Q-value (1 by 2 vector)
    Qvalues=loaded_model.predict(currentState.reshape(1,4))
    # select the action that gives the max Qvalue
    action=np.random.choice(np.where(Qvalues[0,:]==np.max(Qvalues[0,:]))[0])
    # if you want random actions for comparison
    #action = env.action_space.sample()
    # apply the action
    (currentState, currentReward, terminalState,_,_) = env.step(action)
    # sum the rewards
    sumObtainedRewards+=currentReward

env.reset()
env.close()

