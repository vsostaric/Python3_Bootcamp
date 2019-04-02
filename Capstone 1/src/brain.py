import keras
from keras.models import Sequential
from keras.layers import Dense

class Brain:

    def __init__(self):
        self.classifier = Sequential()
        self.classifier.add(Dense(units=5, activation='sigmoid', input_dim=10))
