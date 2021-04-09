/**
 * This file is a serial implementation of Wilson's algorithm on cliques.
 * This will be the basis for an OpenMP solution
 */

#include <iostream>
#include <random>
#include <functional>
#include <chrono>

using namespace std;

// The cliqueSize of this clique
size_t cliqueSize = 100;

// Make a uniform distribution generator
default_random_engine generator(chrono::high_resolution_clock::now().time_since_epoch().count());
uniform_int_distribution<size_t> distribution(0, cliqueSize - 1);

// bind the two together, so that I can do randomVertex() instead of distribution(generator) everytime
auto randomVertex = bind(distribution, generator);

/**
 * Returns a random successor of `node` in `G`
 *
 * Since this is only for cliques, we're really just picking a random element of G
 * that's not equal to node
 */
size_t RandomSuccessor(size_t node) {
	size_t next = randomVertex();
	
	// If we generated ourselves, try again
	if (node == next)
		return RandomSuccessor(node);
	
	return next;	
}

/**
 * root: the number representing the 'root' node
 * n: the number of nodes in this clique
 * G: the graph, which since it's a clique, is just an array of nodes
 */
size_t* randomTreeWithRoot(size_t root, size_t n, size_t* G) {
	// TODO: for now, the *number* = index in the array
	// But this will not be the case in parallel, so I'll need to
	// construct that mapping first

	bool *InTree = new bool[n];
	size_t *Next = new size_t[n];

	for (size_t i = 0; i < n; i++)
		InTree[i] = false;
	
	Next[root] = root; // self-edge root
	InTree[root] = true;

	for (size_t i = 0; i < n; i++) {
		size_t u = i;

		while (!InTree[u]) {
			Next[u] = RandomSuccessor(u);
			u = Next[u];
		}

		u = i;

		while (!InTree[u]) {
			InTree[u] = true;
			u = Next[u];
		}
	}

	delete[] InTree;
	return Next;
}

/**
 * Returns the graphviz of this tree
 */
string printGraphviz(size_t *Next) {
	string result = "digraph G {\n";
	
	for (size_t i = 0; i < cliqueSize; i++) {
		// would use <format>, but this version of g++ doesn't support C++20 :(
		result += "\t" + to_string(Next[i]) + " -> " + to_string(i) + "\n";
	}

	result += "}\n";

	return result;
}

int main() {
	//generator.seed(;
	
	size_t root = randomVertex();
	size_t* tree = randomTreeWithRoot(root, cliqueSize, nullptr);
	cout << printGraphviz(tree) << endl;

	cout << "// root = " << root << endl;
	return 0;
}
