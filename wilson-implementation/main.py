import networkx as nx # Graph library
import random
from timeit import timeit
import time
from statistics import mean, median
from wilson import RandomTreeWithRoot, DrawTree
import numpy as np
import matplotlib.pyplot as plt

# K_5 = nx.complete_graph(5)
# randomSpanningTree = RandomTreeWithRoot(0, K_5)
# DrawTree(list(K_5.nodes), randomSpanningTree, filename="k_5_tree.png")
# 
# K_100 = nx.complete_graph(100)
# randomSpanningTree = RandomTreeWithRoot(0, K_100)
# DrawTree(list(K_100.nodes), randomSpanningTree, filename="k_100_tree.png")


# We want to time, and verify that this is O(n) with complete graphs, O(n^2) with chains, and O(n^3) with lollipops
csv_output = "n,clique,chain,lollipop\n"
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
# root = the root number to start at
# graph_name = name of the gragh, e.g. "complete"
# n = number of vertices
def time_wilsons_algorithm(graph, root, graph_name, n):
    time_array = []

    # we're technically sampling a distribution, so >30 for the central-limit theorem to take effect
    # it's looking like a *super* skewed exponential distribution, so lets do 60 samples to get better
    # results
    for i in range(60): 
        # Q: do I use the same root for every call? Or do I randomly get a new root every time?
        # Let's do both and see what happens
        root = random.randint(0, n-1)
        (_, num_calls) = RandomTreeWithRoot(root, graph)
        time_array.append(num_calls)
    
    plot_histogram(time_array, graph_name, n)
    return mean(time_array)


for i in range(1, 101): # 100 times, each one get's larger
    multiplier = 100
    n = multiplier * i # number of nodes = 100, 200, etc.
    
    # An "n" complete graph is boring
    complete = nx.complete_graph(n)

    # Ditto with a "chain", what network-x calls a "Path graph"
    chain = nx.path_graph(n)

    # An "n" lollipop graph is an n/2 chain followed by a n/2 clique
    lollipop = nx.lollipop_graph(round(n/2), round(n/2)) 
    
    # Since all the graphs are connected, any random vertex (numbered [0, n-1]) 
    # can be the root
    root = random.randint(0, n-1)

    # That doesn't seem to be true -- especially on the lollipop. Choosing a
    # bad root slows it *waaaaaaaaaaaay* down
    # root = 0
    
    work_complete = time_wilsons_algorithm(complete, root, "complete", n)
    work_chain = time_wilsons_algorithm(chain, root, "path", n)
    work_lollipop = time_wilsons_algorithm(lollipop, root, "lollipop", n)

    time_string = f"{n},{work_complete},{work_chain},{work_lollipop}"
    print(time_string)
    csv_output += time_string + '\n'

with open("times.csv") as f:
    f.write(csv_output)
