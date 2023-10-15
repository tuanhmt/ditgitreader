from numpy import exp, array, random, dot

# 3 inputs, one output neural node
synaptic_weights = 2 * random.random((3, 1)) - 1

# Sigmoid (activation function)
def sigmoid(x):
    return 1 / (1 + exp(-x))

# Tinking: multiply inputs with weights
def think(inputs):
    return sigmoid(dot(inputs, synaptic_weights))

# Training data (we'll use these in a bit)
#train_inputs = array([[0.9, 0.1, 0.1], [0.1, 0.6, 0.2], [0.4, 0.1, 0.1], [0.6, 0.8, 0.1]])
#train_outputs = array([[1, 0, 1, 0]]).T

synaptic_weights = [10, -10, -10]

# We now have a node that knows the color red

print("Considering new situation [0.8, 0.3, 0.1] -> ?: ")
print(think(array([0.8, 0.3, 0.1])))

print("Considering new situation [0.2, 0.7, 0.3] -> ?: ")
print(think(array([0.2, 0.7, 0.3])))


