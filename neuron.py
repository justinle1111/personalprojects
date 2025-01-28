import numpy as np

class Neuron:
    def __init__(self, num_inputs):
        self.weights = np.random.randn(num_inputs) * 0.01
        self.bias = 0

    def forward_propagation(self, weights):
        results = np.dot(self.weight, inputs) + self.bias