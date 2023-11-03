from keras.models import Sequential
from keras.layers import Dense
import numpy as np

np.set_printoptions(precision=2, floatmode='fixed', suppress=True)
dataset = np.genfromtxt('water_probability.csv', delimiter=',', dtype=float)
dataset = [:, -1]

for i in range(len(dataset[0]) - 1):
    dataset = dataset[~np.isnan(dataset[:,1])]

dataset = np.around(dataset,2)

Y = dataset[:, -1]
X = dataset[:, :9]

model = Sequential()
model.add(Dense(12, input_dim=9, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.complite(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X,Y, epoches=20, batch_size=100, verbose=2)

print('Предсказание')
prediction_0 = model.prediction(np.array(X[:3]))
prediction_1 = model.predict (x[162:163])
print(prediction_0)
print(prediction_1)
