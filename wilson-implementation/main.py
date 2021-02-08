import networkx as nx # Graph library
import random
from timeit import timeit
import time
from statistics import mean, median
from wilson import RandomTreeWithRoot, DrawTree
import numpy as np
import matplotlib.pyplot as plt
from timing_object import TimingJob

# List all the TimingJobs in this array 
all_graphs = [
    TimingJob("clique", lambda n, params: nx.complete_graph(n)),
    TimingJob("chain", lambda n, params: nx.path_graph(n)),
    TimingJob("lollipop", lambda n, params: nx.lollipop_graph(round(n/2), round(n/2)))
]

# string-ify all the names, comma-separated
all_names = ','.join([g.name for g in all_graphs])

csv_output = f"n, {all_names}\n" 
print("Beginning the timing")
print(csv_output)

# Plots a histogram of the work values, and stores base data
# data = list of scalars
# graph_type = 'name' of the graph, usually "complete", "lollipop", or "path"
# num_vertices = n of graph.
def plot_histogram(data, graph_type, num_vertices):
    # Number of bins should be calculated
    bins = np.histogram_bin_edges(data, bins='auto')

    # I hate MatPlotLib... but it's what every uses :(
    plt.figure() # Required for making a new figure on every use..... cause Matlab...
    plt.xlim([min(data)-5, max(data)+5])

    plt.hist(data, bins=bins, alpha=0.5)
    plt.title(f'Time for {graph_type} n={num_vertices}')
    plt.xlabel('num calls to RandomSuccessor()')
    plt.ylabel('count')

    plt.savefig(f'histogram_{graph_type}_{num_vertices}.png')
    
    with open(f'data_{graph_type}_{num_vertices}.txt', 'w') as f:
        f.writelines("%s\n" % point for point in data)


# Samples the "run-time" distribution of Wilson's algorithm on this graph
# graph = NetworkX graph object
# graph_name = name of the gragh, e.g. "complete"
# n = number of vertices
def time_wilsons_algorithm(graph, graph_name, n):
    time_array = []

    # we're technically sampling a distribution, so >30 for the central-limit theorem to take effect
    # it's looking like a *super* skewed exponential distribution, so lets do 60 samples to get better
    # results
    for i in range(60): 
        # Randomly make a new root on every time
        root = random.randint(0, n-1)
        (_, num_calls) = RandomTreeWithRoot(root, graph)
        time_array.append(num_calls)
    
    plot_histogram(time_array, graph_name, n)
    return mean(time_array)


for i in range(1, 101): # 100 times, each one get's larger
    multiplier = 100
    n = multiplier * i # number of nodes = 100, 200, etc.

    times = [time_wilsons_algorithm(g.make_graph(n), g.name, n) for g in all_graphs]

    time_string = f"{n},{','.join([str(t) for t in times])}"
    print(time_string)
    csv_output += time_string + '\n'

with open("times.csv") as f:
    f.write(csv_output)
