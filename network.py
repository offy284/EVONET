from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
from mscatter import mscatter
import numpy as np


class Network:
    def __init__(self, in_neurons=list(), out_neurons=list()):
        self.in_neurons = in_neurons
        self.out_neurons = out_neurons

        for in_neuron in self.in_neurons:
            in_neuron.outs = list()  # why is this necessary?
            for out_neuron in self.out_neurons:
                in_neuron.project_to(out_neuron)

    def update_inputs(self, activations):
        for i in range(len(activations)):
            self.in_neurons[i].activation = activations[i]

    def print_ins(self):
        out_str = "Inputs: "

        for neuron in self.in_neurons:
            out_str += str(neuron.activation) + " "

        print(out_str)

    def draw_network(self):
        '''
        dot = Digraph()
        dot.node('A', 'A')
        dot.node('B', 'B')
        dot.node('C', 'C')
        dot.edges(['AB', 'AB', 'AB', 'BC', 'BA', 'CB'])

        print(dot.source)
        dot.render("graph.png", view=True)
        '''

        fig = plt.figure()
        ax = plt.axes(projection='3d')

        xdata = []
        ydata = []
        zdata = []
        mdata = []
        adata = []

        neurons = self.in_neurons.copy()
        neurons.extend(self.out_neurons)

        for neuron in neurons:
            xdata.append(neuron.pos[0])
            ydata.append(neuron.pos[1])
            zdata.append(neuron.pos[2])
            if neuron.is_input:
                mdata.append('x')
            elif neuron.is_output:
                mdata.append('o')
            adata.append(neuron.activation)

        xdata.append(0)   # Dummy 1 neuron
        ydata.append(0)
        zdata.append(0)
        adata.append(1)
        mdata.append('^')

        xdata.append(0)   # Dummy 0 neuron
        ydata.append(0)
        zdata.append(0)
        adata.append(0)
        mdata.append('^')

        mscatter(xdata, ydata, zdata, m=mdata, c=adata, cmap='plasma')

        for neuron in neurons:
            for projected in neuron.outs:
                n1 = neuron.pos[0]
                n2 = neuron.pos[1]
                n3 = neuron.pos[2]
                p1 = projected.pos[0]
                p2 = projected.pos[1]
                p3 = projected.pos[2]
                ax.plot([n1, p1], [n2, p2], [n3, p3], color='Grey')

        plt.show()


