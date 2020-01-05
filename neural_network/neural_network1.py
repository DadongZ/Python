import numpy as np

class NeuralNetwork():
    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights = 2 * np.random.random((3, 1))-1

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))
    
    def sigmoid_derivatives(self, x):
        return x*(1-x)

    def train(self, training_inputs, training_outputs, training_iterations):
        for iter in range(training_iterations):
           outputs = self.think(training_inputs)
           error = training_outputs - outputs
           adjustments = error * self.sigmoid_derivatives(outputs)
           self.synaptic_weights += np.dot(training_inputs.T, adjustments)

    def think(self, input):
        return self.sigmoid(np.dot(input.astype(float), self.synaptic_weights))

if __name__=="__main__":
    neural_network = NeuralNetwork()
    print('Random starting synaptic weight: ')
    print(neural_network.synaptic_weights)

    training_inputs = np.array([[0, 0, 1],
                                [1, 1, 1],
                                [1, 0, 1],
                                [0, 1, 1]])

    training_outputs = np.array([[0, 1, 1, 0]]).T

    neural_network.train(training_inputs, training_outputs, 1000)

    print("Synaptic weigth after training: ")
    print(neural_network.synaptic_weights)

    A = str(input("Input 1: "))    
    B = str(input("Input 2: "))    
    C = str(input("Input 3: "))    

    print("New situation: input data = ", A, B, C)
    print("Output: ")
    print(neural_network.think(np.array([A, B, C])))