# import the necessary libraries
import numpy as np
import random
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop
from collections import deque
from tensorflow import gather_nd
from tensorflow.keras.losses import mean_squared_error

class DeepQLearning:
    def __init__(self, env, gamma, epsilon, numberEpisodes, num_samples, num_traffic_analyzer):
        self.env = env
        self.gamma = gamma
        self.epsilon = epsilon
        self.numberEpisodes = numberEpisodes
        self.stateDimension = num_samples * 2
        self.actionDimension = 3
        self.replayBufferSize = 300
        self.batchReplayBufferSize = 100
        self.counterUpdateTargetNetwork = 0
        self.sumRewardsEpisode = []
        self.replayBuffer = deque(maxlen=self.replayBufferSize)
        self.mainNetwork = self.createNetwork()

    def my_loss_fn(self, y_true, y_pred):
        s1, s2 = y_true.shape
        indices = np.zeros(shape=(s1, s2))
        indices[:, 0] = np.arange(s1)
        indices[:, 1] = self.actionsAppend
        loss = mean_squared_error(gather_nd(y_true, indices=indices.astype(int)), gather_nd(y_pred, indices=indices.astype(int)))
        return loss

    def createNetwork(self):
        model = Sequential()
        model.add(Dense(128, input_dim=self.stateDimension, activation='relu'))
        model.add(Dense(56, activation='relu'))
        model.add(Dense(self.actionDimension, activation='linear'))
        model.compile(optimizer=RMSprop(), loss=self.my_loss_fn, metrics=['accuracy'])
        return model

    def trainingEpisodes(self, num_samples, num_traffic_analyzer):
        for indexEpisode in range(self.numberEpisodes):
            rewardsEpisode = []
            print("Simulating episode {}".format(indexEpisode))
            (currentState) = self.env.reset(num_samples, num_traffic_analyzer)
            print("Current state {}".format(currentState))
            terminalState = False
            while not terminalState:
                action_0 = self.selectAction(currentState, indexEpisode)
                action = (action_0[0], action_0[1], action_0[2][0].item())
                action_0[2][0] = round(action_0[2][0].item(), 2)
                nextState, reward, terminalState = self.env.step(action)
                rewardsEpisode.append(reward)

                 # Reshape currentState to match your network's input shape
                currentState = currentState.reshape(1, 6) # numple_samples * 2
                nextState = nextState.reshape(1, 6)
                # làm sao để action có thể được làm tròn trước khi đưa vào đoạn này
                self.replayBuffer.append((currentState, action, reward, nextState, terminalState))
                self.trainNetwork()
                currentState = nextState
            print("Sum of rewards {}".format(np.sum(rewardsEpisode)))
            self.sumRewardsEpisode.append(np.sum(rewardsEpisode))

    def selectAction(self, state, index):
        print("index: ", index)
        if index < 1:
            # Randomly sample actions for each component of the multi-discrete action space
            return (self.env.action_space[0].sample(), self.env.action_space[1].sample(), self.env.action_space[2].sample())
        
        randomNumber = np.random.random()
        
        if index > 200:
            self.epsilon = 0.999 * self.epsilon
            
        if randomNumber < self.epsilon:
            # Randomly sample actions for each component of the multi-discrete action space
            return [self.env.action_space[0].sample(), self.env.action_space[1].sample(), self.env.action_space[2].sample()]
        
        # Use your Q-network to select actions for each component of the multi-discrete action space
        Qvalues = self.mainNetwork.predict(state)
        action_1 = np.random.choice(np.where(Qvalues[0][0] == np.max(Qvalues[0][0]))[0])
        action_2 = np.random.choice(np.where(Qvalues[0][1] == np.max(Qvalues[0][1]))[0])
        action_3 = np.random.choice(np.where(Qvalues[0][2] == np.max(Qvalues[0][2]))[0])
    
       
        print("Qvalues: ", Qvalues)
        print("action_1: ", action_1)
        print("action_2: ", action_2)
        print("action_3: ", action_3)

        return (action_1, action_2, action_3)

    def trainNetwork(self):
        if len(self.replayBuffer) > self.batchReplayBufferSize:
            randomSampleBatch = random.sample(self.replayBuffer, self.batchReplayBufferSize)
            currentStateBatch = np.zeros(shape=(self.batchReplayBufferSize, 6))
            nextStateBatch = np.zeros(shape=(self.batchReplayBufferSize, 6))
            for index, tupleS in enumerate(randomSampleBatch):
                currentStateBatch[index, :] = tupleS[0]
                nextStateBatch[index, :] = tupleS[3]
            QnextState = self.mainNetwork.predict(nextStateBatch)
            QcurrentState = self.mainNetwork.predict(currentStateBatch)
            print("Shape of QcurrentState: ", QcurrentState.shape)
            inputNetwork = currentStateBatch
            outputNetwork = np.zeros(shape=(self.batchReplayBufferSize, 3))
            self.actionsAppend = []
            for index, (currentState, action, reward, nextState, terminated) in enumerate(randomSampleBatch):
                if terminated:
                    y = reward
                else:
                    y = reward + self.gamma * np.max(QnextState[index])
                self.actionsAppend.append(action)
                action_array = [int(action[0]), int(action[1]), int(action[2] * 100)] 

                outputNetwork[index] = QcurrentState[index]
                outputNetwork[index, action[0], action[1], int(action[2] * 100)] = y
                

            self.mainNetwork.fit(inputNetwork, outputNetwork, batch_size=self.batchReplayBufferSize, verbose=0, epochs=100)
