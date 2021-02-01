import networkx as nx # Graph library
import matplotlib.pyplot as plt
import random
from timeit import timeit
import time
from statistics import mean

# Function implementations from the paper

# Returns a random neighor of node in G
def RandomSuccessor(node, G):
    neighbors = [neighbor for neighbor in nx.neighbors(G, node)]
    # print(f'Neighbors of {node}: {neighbors}')
    return random.choice(neighbors)

# Runs the easier version of the algorithm: we know what the root of the tree is
def RandomTreeWithRoot(r, G):
    n = nx.number_of_nodes(G)
    InTree = dict()
    Next = dict()
    for node in nx.nodes(G):
        InTree[node] = False
        Next[node] = ""

    InTree[r] = True

    for i in nx.nodes(G):
        u = i

        while (not InTree[u]):
            Next[u] = RandomSuccessor(u, G)
            u = Next[u]

        u = i

        while (not InTree[u]):
            InTree[u] = True
            u = Next[u]

    return Next


def DrawTree(graphNodes, randomSpanningTree, filename="tree.png"):
    Tree = nx.Graph()
    Tree.add_nodes_from(graphNodes)
    edges = []
    for (key,value) in randomSpanningTree.items():
        if value != "":
            edges.append((key, value))

    Tree.add_edges_from(edges)

    nx.draw(Tree, with_labels=True)
    plt.savefig(filename)


# create the graph
G = nx.Graph()

graph1Nodes = ["Denver", "Lakewood", "Golden", "Arvada", "Aurora", "Centennial", "Littleton", "Thornton", "Boulder"]
graph1Edges = [("Denver", "Lakewood"), # US6
               ("Denver", "Aurora"), # I70
               ("Denver", "Arvada"), # I70
               ("Denver", "Thornton"), # I25
               ("Denver", "Boulder"), # US36
               ("Denver", "Centennial"), #I25
               ("Denver", "Littleton"), # Sante-Fe
               ("Lakewood", "Golden"), # US6
               ("Lakewood", "Littleton"), # C470
               ("Lakewood", "Arvada"), # I70
               ("Littleton", "Centennial"), # C470
               ("Golden", "Boulder"), #C93
               ("Thornton", "Aurora"), # E470
               ("Thornton", "Boulder") # Northwest Parkway
               ]


G.add_nodes_from(graph1Nodes)
G.add_edges_from(graph1Edges)


# draw the graph
#nx.draw(G, with_labels=True)
#plt.savefig("graph.png")

# Get and draw the resulting graph
# randomSpanningTree = RandomTreeWithRoot("Golden", G)


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

def time_function_10_times_and_take_average(function):
    time_array = []
    for i in range(10):
        start = time.time()
        function()
        time_array.append(time.time() - start)

    return mean(time_array)


for i in range(1, 101): # 100 times, each one get's larger
    multiplier = 1000
    n = multiplier * i # number of nodes = 100, 200, etc.
    
    # An "n" complete graph is boring
    complete = nx.complete_graph(n)

    # Ditto with a "chain", what network-x calls a "Path graph"
    chain = nx.path_graph(n)

    # An "n" lollipop graph is an n/2 chain followed by a n/2 clique
    lollipop = nx.lollipop_graph(round(n/2), round(n/2)) 
    
    # Since all the graphs are connected, any random vertex (numbered [0, n-1]) 
    # can be the root
    # root = random.randint(0, n-1)

    # That doesn't seem to be true -- especially on the lollipop. Choosing a
    # bad root slows it *waaaaaaaaaaaay* down
    root = 0
    
    # time_complete = time.time(lambda: RandomTreeWithRoot(root, complete))
    # start = time.time()
    # RandomTreeWithRoot(root, complete)
    # time_complete = time.time() - start
    time_complete = time_function_10_times_and_take_average(lambda: RandomTreeWithRoot(root, complete))

    # time_chain = time.time(lambda: RandomTreeWithRoot(root, chain))
    # start = time.time()
    # RandomTreeWithRoot(root, chain)
    # time_chain = time.time() - start
    time_chain = 0 # time_function_10_times_and_take_average(lambda: RandomTreeWithRoot(root, chain))

    # time_lollipop = time.time(lambda: RandomTreeWithRoot(root, lollipop))
    # start = time.time()
    # RandomTreeWithRoot(root, lollipop)
    # time_lollipop = time.time() - start
    time_lollipop = 0 # time_function_10_times_and_take_average(lambda: RandomTreeWithRoot(root, lollipop))

    time_string = f"{n},{time_complete},{time_chain},{time_lollipop}"
    print(time_string)
    csv_output += time_string + '\n'

with open("times.csv") as f:
    f.write(csv_output)
