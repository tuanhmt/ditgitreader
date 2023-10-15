from numpy import exp, array, random, dot

random.seed(1)

# 3 inputs, one output neural node
synaptic_weights = 2 * random.random((3, 1)) - 1

# Sigmoid (activation function)
def sigmoid(x):
    return 1 / (1 + exp(-x))

# Derivative of the Sigmoid function, used to adjust error
def sigmoid_derivative(x):
    return x * (1 - x)

# Training the Neural net with a set of inputs with known outputs
def train(train_inputs, train_outputs, iterations):
    global synaptic_weights
    for iteration in range(iterations):
        output = think(train_inputs) # training: multiply the weights with the inputs
        error = train_outputs - output # see what the error is
        adjustment = dot(train_inputs.T, error * sigmoid_derivative(output)) # calculate the adjustments
        synaptic_weights = synaptic_weights + adjustment # modify the weights with these adjustments

# Tinking: multiply inputs with weights
def think(inputs):
    return sigmoid(dot(inputs, synaptic_weights))

# Training data
train_inputs = array([[0.9, 0.1, 0.1], [0.1, 0.6, 0.2], [0.4, 0.1, 0.1], [0.6, 0.8, 0.1], [0.1, 0.1, 0.9]])
train_outputs = array([[1, 0, 1, 0, 0]]).T

# The weights before training
print("Synaptic weights before training: ")
print(synaptic_weights)

# Do this a few times
train(train_inputs, train_outputs, 10000)

# The weights after training
print("Synaptic weights after training: ")
print(synaptic_weights)

# We now have a node that knows the color red

print("Considering new situation [0.8, 0.3, 0.1] -> ?: ")
print(think(array([0.8, 0.3, 0.1])))

print("Considering new situation [0.2, 0.7, 0.3] -> ?: ")
print(think(array([0.2, 0.7, 0.3])))

print("Considering new situation [0.2, 0.1, 0.8] -> ?: ")
print(think(array([0.2, 0.1, 0.8])))

