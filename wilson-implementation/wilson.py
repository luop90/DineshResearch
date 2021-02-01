import networkx as nx
import random
import matplotlib.pyplot as plt


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
    num_calls = 0 # Used to measure the number of calls to RandomSuccessor(), a better measurement of work than timing [as timing gets into cache stuff]

    for node in nx.nodes(G):
        InTree[node] = False
        Next[node] = ""

    InTree[r] = True

    for i in nx.nodes(G):
        u = i

        while (not InTree[u]):
            Next[u] = RandomSuccessor(u, G)
            num_calls += 1
            u = Next[u]

        u = i

        while (not InTree[u]):
            InTree[u] = True
            u = Next[u]

    return (Next, num_calls)

# Draw the tree using their in-house drawing function (which isn't very good TBH)
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

