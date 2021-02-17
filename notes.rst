Project vs Thesis
=================
6 credits vs 9 credits of research

Thesis

Dinesh views this as changable

Theoretical vs Applied
======================
Jack made AlgoBOWL as his project.

With a theory project, "originality" is a major factor.
* "Chasing the literature"
* A large part is arguing that what you've done is original / no one else has done it

Network Science
===============
All of these "metrics" (e.g. the Mantel test) were developed early on small (n = 12) data sets. We want to apply these to "Big Data"

Cheminformatics: take a molecule, which is really just a connected graph (usually a tree, but sometimes not), generate all the isomers of nicotine.
* Enumerating isomers is well known
* Gave a "distance metric" and got a network of metrics.
* This is where the Mantel test came out. But with large n, this takes too long.

Looking at parallel random spanning tree over Winter Break?

Network Science: they have various metrics to make assessments about networks. Is it... reliable, etc.
* "Betweenness Centrality Metric": similar to the idea of the articulation vertex.
  * All pairs of paths/vertices in a network
  * Trying to find the shortest path between source & destination pairs
  * ...which vertices does this path go through? A very central vertex has high "importance" since many paths go through it.
  * This is easily N^2. Can this be approximated without much work?
  * Would a randomized version give an *almost* equally good answer, but takes a lot less time? (Instead of all source/destination pairs)
  


AlgoBOWL
========
(1) Put it on a better server than just the CS Mines server

(2) Jack thought this was doable, people upload their programs, and the server executes it. That way runtime makes a play

(3) There's a lot of practical solutions to NP-Hard problems. Maybe try to find a benchmark (or beg the other research team with their code, or implement yourself),
and compare their implementation to yours.

Say the TSP problem, we pre-load a bunch of inputs, someone comes up with a new algorithm and uploads it, the server runs their input and takes the results
(or runs like 10 times?)

Right now there's no "public" benchmark to compare. Everyone just takes someone's word for it. This is far larger than just AlgoBOWL.

This could be very valuable in the expirmental algorithms community. It's about getting better runtimes on various inputs. This is very, very applied. And somewhat
of a sales job to get people to adobt it.

This would have to be hosted on the cloud + architectural questions (how to run things to ensure runtimes are correct).

We could run this by Jack and see how "crazy" of an idea this is.


MazeGenerators
==============

Add infrastruture to generate Mazes? Some cabaility that makes it more meaningful for students.

Want to create a *good* maze (e.g. only 1 solution). He doesn't think this is a difficult task, besides just sitting down and doing it.

Beyond that one addition, is there something creative we can do with it, to make it more fun / better pedogogically meaningful?
Classical problem: not listening to instructions to convert the maze to a plain (boring) graph and run BFS, they're attacking it directly.






Summary
=======
See if we can narrow down on something.

Muddle around on the internet, talk to Jack, we should try to narrow down the focus a little bit.


Next Day
========

Someone must have tried to find a randomized centrality algorithm, how does it perform?
* Compare rankings to the full V^3 algorithm
* Some stuff has probably been done, but we can find something novel to do.

Use Google Scholar
* Typing things in here about 'Centrality'
* If you find a good paper, you can see who cited this paper (forward reference)


Between Centrality is easy to find
* Look at NetworkX (or another metric), find their implementation of betweenness-centrality
* Give it 50 vertices, etc.

Improve run-times / speeds (as N^3 is not reasonable). We mention N but we might want to do better than N.
* parallel construction of spanning trees / uniform spanning trees
* Mantel paper -- can we parallel the randomized spanning tree / how difficult would it be to implement / can we do it with GPUs?
  * Based on random walks, which is hard to parallelize.
  
Possible research paths:
* Centrality stuff?
* Parallel implementation of random spanning trees. This isn't really looking at Network Science
  * See theortical references that describe the spanning tree algorithm.
  * Foward-search on those paper.
  * See who has even used uniform random spanning trees.
    * "There's a lot of theory that doesn't get used"
    

* Contact Dorothy about "advisor paperwork"

Next Steps:
(1) Read the linear time paper & play with some examples
(2) Forward-reference it and find what people have done with that paper
(3) See if someone has managed to parallelize random walks.
(4) Read the network science book?
(5) Find stuff on centrality...?


Next Steps:
(1) Read the introduction and try to explain the paper in an undergraduate level.
-> Is there something worthwhile we can grab from the random walk?
(2) 4 random walks that connect... definitely a spanning tree. Is it uniform random though?
-> Dive into Wilson's proof on uniformness.
(3) Look into the algorithms that Wilson improved upon. Maybe those are easier to parallel?
(4) Plan F --- implement a parallel spanning tree that might not even be random, but does it work? I.e. no theoritical backend, but applied.
-> Not what we should shoot for.
-> Can't prove it mathematically, but with a bunch of experiments, does it seem to work statistically?
-> Devise some sort of statistical tests for random spanning trees, and say we're doing okay.
-> How do you prove something is random? This gives us a reassurance of a backup strategy.

Maybe ~1 month? on plan A. In the context of a thesis, need to understand the literature. A "Lit survey" section (A chapter, 5 - 10 pages, describe work that has been done.)


Summary of the Introduction:
----------------------------
A (stupid?) random walk is omega(m * n):
(1) start at this vertex
(2) follow *any* edge you want, keeping track of the edges you follow
(3) Halt when you have reached every vertex.

The "transcript" / log of where the random walk went can be used to determine an arborescence of T.
=> But this walk is stupidly slow. You'll make omega(m*n) steps, but only need O(n) of those.
=> Can we speed this up by "shortcutting" where the walk goes?
    ...yes..

But I don't see how this is better than Wilson's algorithm.

TL;DR, I don't see how this is useful. But it was a lot of fun to learn.


Next Steps
----------
(1) Is Wilson's algorithm O(n)? Or O(m n), like everyone is claiming.
  -> Is it just O(n) on complete graphs? Even though m = n^2
  -> See Wilson's analysis.

(2) Maybe read the introduction of the "crazy distributed papers" to see if there's a practical algorithm we can implement.
  -> This is not trivially parallelize-able. But Mehmet seemed on-board with the "100-ants crawling the graph" approach.

Partition the graph, each ant gets its own partition, and only needs to synchronize when you get to a "boundary" vertex or edge.
-> Assume complete? Then every vertex is a boundary vertex (*lots* of synchronization).
-> Assume sparse? But then how can we ensure that each partition is connected?
  -> Mehmet might have some idea. Or maybe Bo?
  -> Or look at papers to find partitioning algorithms.
    -> "Spectral Partitioning Algorithms", might not be the best though.


(4) Talk to Mehmet about what this graph scheduling thing is. I should really choose by mid-Febuary.
  -> Dinesh thinks someone would have done this before, in the VLSI synthesis community. "High-level synthesis"
    -> It will be a heuristic, but Dinesh thinks it'll be a fairly good one. That's his "gut feeling"
  -> Mehmet doesn't really care about this from the theory point of view, he just wants a working implementation.


Notes from Mehmet
-----------------
* Critical path may change based on where you schedule the kernals / processes, since by assigning the critical path to the fastest
machines may change what the critical path actually is.
* Dinesh recommended high-level synthesis. Maybe look into that?

Also see the springer book here: https://www.springer.com/gp/book/9783540695158. Might be useful?


Notes
-----

* "The running time is linear in the number of calls to RandomSuccessor"
  * His actual algorithm is O(tau), where tau is this crazy thing
  * How does tau relate to n or m...? Best I can find is a lower-bound.
    * tau >= n - 1 /2
    * He doesn't mention an upper bound from what I can see.

* How on earth could this algorithm be anything *but* O(n)??
  * Looks like he dives into "proper" random sampling, and how apparently that is kinda hard.
  * I *think* that if you assume RandomSuccessor is O(1), then we get O(n) performance.
    * ...but you can get loops. While these loops are eventually erased, you could do a lot of excess work with them.

* Cover time of a clique - O(n log n) [coupon collector]
* Hitting time -- looks to be 2*m? Hard to find an answer here.
  * See Hitting Time lecture slides, they make it sound like the "expected path length" = 2m (= hitting time?)

* Idea: I have working code. I can generate complete graphs of arbitrary size. Why not see if we can experimentally verify the running time?

* Idea for randomness: "reduce" to generating random numbers of the range 0 -> # of spanning trees, and number all of them. Then we're looking at generating
random numbers of the range [0, # of spanning trees)
  "posterioi check"
  * need a correspondance between spanning trees and numbers.
  * something out of combinatorics to view a spanning tree as an array of numbers.
  * Dinesh has another book on "spanning trees as integers"

Next Steps
----------
(1) Some background work on still convincing us that this is O(n) for complete graphs
  * 1 million times of collecting numbers of K_100 or something? Make sure it looks linear.
  * Experimentally, what occurs when the graph is *not* complete. Say, a lollipop.
    * Confirm O(n^2) for chains, and O(n^3) for lollipops.
    * Lets get a sense of runtimes on these other graphs. At the end of the day, we want to test this on realistic graphs.

(2) Randomness with QQPlot?

(3) Tradeoff looks to be coming down between runtime and randomness.
  * If we split it off, how *unrandom* is it.
  * If we do random partitions, does that help fix the problem?
  * Possible thesis: I want a random spanning tree that's fast, in parallel, and I don't *quite* care about perfectly random.

(4) Models on graph generation
  * "Preferential attachment"? Albert & Barabasi. See Network Science book -- maybe Network-X implements one of these?
  * Generate graphs that appear real world, and see how it performs.

(5) Read Circuit Synthesis book. See if it might be useful.

(6) Read paper Dinesh sent over

Notes
-----
(1) When implementing the timing, the time seems to be *significantly* dependent on what the root is (for chain & lollipop, doesn't matter on clique).
  * When doing root = random(), it was: clique < chain < lollipop (as expected)
    * ...but, lollipop() was taking exponential time on ~1/3 runs. As in, went from 0.03, to over 3 seconds, to over 3 minutes (before I killed it)
  * When doing node = 0, the timing was: clique < lollipop < chain (i.e. the chain became significantly worse)
  * There's also a *lot* of variability in these numbers. Which I guess kind-of makes sense, based on the random nature.
  
* I also did some research into hitting time and found a paper by Karp. WRITE MORE ABOUT THIS

(6) I scanned through the paper Mehmet gave, and it absolutely looks like what he was going for (at least, from the little bit I know)


Next Steps
----------
(1) Has anyone looked into the variance of the hitting time?
-> No. But I *did* find a paper that agreed with your conclusion of O(n) for hitting time on a clique.
-> Page 3 (last paragraph) of "max hit" mentions the expected hitting time of a lollipop is 4 n^3 / 27, i.e. O(n^3) [I've seen that number float around]
-> Page 4 (second paragraph from the bottom) does the same analysis for a clique, and finds the expected time to be n-1, i.e. O(n).

...So I think we can finally rest our case that Wilson's algorithm is O(n) on cliques.
-> This was published in 1990.

I found a second paper that also, more formally, gives hitting time on a clique to be O(n).
-> tr1029.pdf
-> Published in 1993.
-> Halfway down page 7, gives an infinite sum that converges to n-1. They don't explain where the sum comes from as "it is clearly <X>"
   but it appears to match what you give in your paper.
-> I verified their math with Mathematica, and it checks out.

-> (n-2/n-1)^t-1 == went to the *incorrect* node t-1 times. Occurs with P(n-2/n-1): went to any node besides your current node (no self edges) and the one you want
-> But then why multiply by t?

(2) Look at chain vs clique runtimes. Is there an implementation problem?
-> Should we be picking a random node? I think we *should* be. Doesn't really matter with the clique, but really matters with the other two.
-> maybe try to visualize this? Maybe see any videos about output of a random walks.

-> More formal graphs, different values of n, "more formal runtime analysis"
-> Spend more time on chains and lollipops -- why are they worse?

=> Run-times look good, with my modifications (e.g. picking a new, random root *every* time)

(3) Look into the "random graph generators", and what the graphs are.

(4) Add Karp to drive [Done]

(5) Schedule meeting w/ Mehmet about that paper his sent. Maybe have a more comprehensive meeting w/ Dinesh?
-> Does it meet his needs? Or is there something missing?

(6) Can Bo point us in the right direction for dealing with graphs on GPUs?

(7) Graph algorithms on FPGAs.
-> Usually just on "nice" graphs. E.g. grids or convolution via a 3x3 matrix.
-> Different story if they could pull this off on say, betweenness-centrality.
-> On GPUs instead?

(8) Paper -- assuming all possible paths are already present in the graph
* Tasks graph doesn't change, but the computation graph can change
* Generate all possibilities of task graph vs engine, and generate all possible paths

Weight of nodes/edge = dynamic
Cannot find critical path easily


The task graph itself doesn't change, but the target node is changing. This isn't in their case.
* Node weights can change
* Also different paths can be exected in parallel
* Graph partition?
* Dynamically changing vertex weights, but the topology itself doesn't change.

What's Next?
------------
* Parallel random walks?
* Is it even possible to simulate this?
  * Partition into 8 graphs, and then do 8 hops at a time. Synchronize when they cross into the other graph (really bad on a clique)
  * Ideally we'd do this on a realistic graph (so power laws, preferential attachment, etc.)
  * Generate other graphs, and see where they fit in w.r.t lollipop, clique, and path.
    * Hitting time of preferential attachment?
* Maintain a TODO list of things one *can* do, whether or not we actually do them. Maybe a few baby steps on each one, we could figure out how to do some of this theoritically.


TODO List:
----------
(1) See where graph generators fit in / social networks.
(2) Variance of hitting time?
(3) Parallel random walks
  -> On a clique: sequential works well, but parallel seems to be a disaster
  -> On a lollipop: sequential is a disaster. Might it weirdly become better for a parallel?
(4) Scheduler
(5) Making a script that somehow tests uniform random.
        -> I started a script that did this based on the GraphTheory book but actually need to finish it


Next Steps
----------
(1)
-> Formulated a decent setup for easily adding on more graphs to compare against.
-> Next step: actually time some.

(2) -- see if parallel can help. Make sure it passes the "smell" test.

(3) Continue w/ the "mid-week" email so he can prep for this meeting.

(4) Read Mehmet's paper
-> Read and sent him an email confirming it.
-> Next step: read the book Dinesh sent

Wednesday ToDos:
        (1) Start timing other network graphs
                -> It seems like, in general, preferential attachment is much closer (in times) to the clique, rather than the other two.
                -> Definitely based on the number of edges per node though...
        (2) Finish uniform-random script
        (3) ...if time, look into finding the distribution of the variance??? Fitting distribution might be a neat thing to google.
        (4) Send an email to Dinesh so he knows what to expect for our meeting.
        (5) Send Mehmet relavent pages of their paper
        (6) Start working on a brute-force approach? I'll need to confirm the API with Mehmet...



Next Steps
----------

(1) Time even more types of graphs. Use both random models and real graphs. Must be undirected. 

(2) Theortically, are there graphs that are known to be O(n), from Theory?

(3) Scheduling problem: let's formally define the problem in a way that would make theorists happy. HPC-DAG is my current name for it.

(4) Time to start thinking about how to do this in parallel. Before we go to a GPU, conceptually, how would we do this.
-> Synchronize on "bump"?
-> Or, just cycle erase / overwrite on bump?
-> Record which processor visited the vertex?
        -> Do we care who wins about race conditions?

(a) Make something that generates *a* spanning tree first.
        (i) Do we have *one* tree, or *multiple* trees that are being constructed?
                * Two random walks coming back to one tree, or two random walks each making their own tree

                * One random walk:
                        One tree, two walks. They synchrnoize *not* when they cross, but rather when one reaches the tree.

                      * Pseudocode first

(b) Then we make it better.
        (i) Faster
        (ii) More random
        (iii) etc...

(5) Background work: get this "Verifier" script that we are getting uniform random trees.



Work Done
---------

From (4):

* I've done everything in Python, which has something called the *Global Interpreter Lock* -- I.e., it does *not* support parallelism. Only 1 thread can run at a time, so you get *concurrency*, but not *parallelism*

        * ...but that is only true "out of the box". I don't think concurrency gives us much of an improvement, as graph access looks effectively random in memory. 

        * There also exists a module called ``multiprocessing`` which effectively side-steps GIL by spawning new processes, as GIL means threads *within* a process only actually run one at a time, but that is not true across processes: processes can run in parallel if there's >1 CPU.


        * ...all that being said, I'm starting to implement multi-threads *first* (using Locks), as that will give me a good sense of what I'll have to work with moving forward

                * While I have never taken a parallel programming class, I have all the lecture notes, and I'm learning a *bunch* about this. I'm just still kicking myself for not taking it last year :(

                * I'm basically following the "shared address space" model:
                        
                        * The graph is immutable

                        * The "tree" is effectively a big bulletin board, with locks around updating it.


        * Different parallel models I could go with -- do you have an opinion?

                (1) Shared address space model:
                        
                        (a) Graph is global, immutable. "tree" is global, *mutable*, but updating requires locks.
                        (b) Threads have their own private 
