
# This class represents all the graphs that should be timed
class TimingJob:
    # name - string representation of this graph
    # generator - a function given the parameters (n, set_parameters=dict()) -> network-x graph
    # set_parameters - dict()
    def __init__(self, name, generator, set_parameters=dict()):
        self.name = name
        self.generator = generator
        self.set_parameters = set_parameters
    
    # Calls the generator with "n", and it's given parameters
    # Returns a network-x graph
    def make_graph(self, n):
        return self.generator(n, self.set_parameters)
