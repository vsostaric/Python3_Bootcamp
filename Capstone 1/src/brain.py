import keras
from keras.models import Sequential
from keras.layers import Dense

class Brain:

    def __init__(self):
        self.neural_network = Sequential()
        self.neural_network.add(Dense(units=5, activation='sigmoid', input_dim=10))
        self.neural_network.add(Dense(units=5, activation='sigmoid'))
        self.neural_network.add(Dense(units=1, activation='sigmoid'))
        self.neural_network.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
