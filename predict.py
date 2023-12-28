from keras import layers
import tensorflow as tf
import numpy as np
import keras
from sklearn.model_selection import train_test_split

def load_data(file_name) -> np.array:
    with open(file_name, "r") as file:
        data = [line.split(",") for line in file.read().split("\n")[1:-1]]
        x = np.array([np.array(list(map(float, line[3:-1]))) for line in data])
        y = np.array([np.array([float(line[-1])]) for line in data])

    return x, y


X, Y = load_data("processed_polynomial_output.csv")
print(X, Y)
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=1)

model = keras.Sequential()
model.add(keras.Input(shape=(7,)))
model.add(layers.Dense(10, activation="relu"))
model.add(layers.Dense(10, activation="relu"))
model.add(layers.Dense(10, activation="relu"))
model.add(layers.Dense(1, activation="tanh"))

model.compile(optimizer="adam", loss="mean_absolute_percentage_error", metrics=["accuracy"])

model.fit(x_train, y_train,
          batch_size=32,
          epochs=500,
          verbose=1,
          validation_data=(x_test, y_test))

score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
