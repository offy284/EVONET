class Network:
    def __init__(self, in_neurons=list(), out_neurons=list()):
        self.in_neurons = in_neurons
        self.out_neurons = out_neurons

        for in_neuron in in_neurons:
            for out_neuron in out_neurons:
                in_neuron.project_to(out_neuron, distance=1)

    def update_inputs(self, activations):
        i = 0
        for neuron in self.in_neurons:
            neuron.activation = activations[i]
            i += 1

    def print_ins(self):
        out_str = "Inputs: "

        for neuron in self.in_neurons:
            out_str += str(neuron.activation) + " "

        print(out_str)