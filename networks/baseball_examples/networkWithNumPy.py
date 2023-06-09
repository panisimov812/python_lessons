import numpy as np

weights = np.array([0.1, 0.2, 0])


def neural_network(input, weights):
    pred = input.dot(weights)
    return pred


# текущее среднее число игр сыгранное игроками
toes = [8.5, 9.5, 9.9, 9.0]
# текущая доля игр, окончившихся победой (процент)
wlrec = [0.65, 0.8, 0.8, 0.9]
# число болельщиков
nfans = [1.2, 1.3, 0.5, 1.0]

input = np.array([toes[0], wlrec[0], nfans[0]])
pred = neural_network(input, weights)
print(pred)