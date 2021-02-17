import networkx as nx # Graph library
import random
from statistics import mean, median
from wilson import RandomTreeWithRoot, DrawTree
import numpy as np
import matplotlib.pyplot as plt

# From Cayley's formula, we know there are n^(n-2) spanning trees of a complete graph with n vertices
# So we're going to attempt to verify that we are generating them all with equal probability.

""" Overall idea:
    - We can generate a unique sequence for every tree
    - We know there are going to be n^(n-2) trees
    
    (0) Choose an `n`. Generate a clique of size n
    (1) Generate, say, 30*# of trees, using Wilson's algorithm (30 comes from central limit theorem)
    (2) For every tree, generate its integer sequence
    (3) "Sort" the integer sequence (concatenate the sequence to be strings, and then sort?)
        * The index in the sorted list is the "number" from 0 -> n^(n-2) that represents this tree
    
    This script is effectively a blackbox that generates random integers from [0, n^(n-2)), so
    if Wilson's algorithm (or whatever we devise) is actually uniform random, then a QQPlot should
    "prove" that we are actually sampling numbers from the uniform random distribution [0, n^(n-1))
"""


# This function returns the sequence (list) of numbers representing the tree
# Following the construction given in 10-2 of Graph Theory by Deo
# tree - a network-X graph representing a tree.
# root - the label of the root node
# returns a list of integers
def construct_sequence_of_labeled_tree(tree, root):
    # "pendant" vertex == vertex of degree 1 (for a tree, this can only be a leaf)
    # every (n>=2) tree has at least 2

    # (1) find the pendant vertex with the smallest label, call it a1
    # (2) call a1's only neighbor b1. Add b1 to the sequence
    # (3) Remove a1.
    # Repeat until there are only 2 vertices remaining.
    # This gives a unique sequence representing the tree


# pytest might be a good idea... but here's the example tree the book uses
G = nx.Graph()
G.add_edges_from([(1,2), (1,4), (1,3), (3,5), (5,6), (5,7), (5,9), (9, 8)])
expected_sequence = [1,1,3,5,5,5,9]
