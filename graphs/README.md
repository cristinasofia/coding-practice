# Disjoint Sets
The idea behind partitioning a set S into N disjoint subsets S_0, S_1, . . . S_N−1, where disjoint means that
1. every element x is an element of some subset S_i, and
2. that no element in subset S_j is found in another subset S_k.

Equivalently, you can say that for all i != j, then the intersection of S_i and S_j is the empty set.

Equivalence relations:
- Reflexivity: a relates to a.
- Symmetry: if a relates to b, then b relates to a.
- Transitivity: if a relates to b and b relates to c, then a relates to c.

## Union Find
```python
def find(x):
	if a[x] < 0:
		return x
	else:
		return a[x] = find(a[x])
```
https://leetcode.com/problems/friend-circles/
https://leetcode.com/problems/redundant-connection/
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
https://leetcode.com/problems/number-of-operations-to-make-network-connected/
https://leetcode.com/problems/satisfiability-of-equality-equations/
https://leetcode.com/problems/accounts-merge/
https://leetcode.com/problems/connecting-cities-with-minimum-cost/

# Graphs
## Terms
A graph G is a set of vertices and edges, (V, E). Edges connect vertices, and thus are a pair(u, v) where u, v ∈ G.
1. **Undirected vs. Directed:** A graph is undirected if edge (x,y) ∈ G implies (y,x) ∈ G.
2. **Weighted vs. Unweighted:** A weighted graph assigned a weight to each vertex or edge. An unweighted graph would assign a boolean value (e.g., matrix of only 0s and 1s).
3. **Simple vs. Non-simple:** A simple graph does not contain loops or multiedges.
4. **Cyclic vs. Acyclic:** An acyclic graph does not contain any cycles.
   - Trees are connected, acyclic undirected graphs.
   - Directed acyclic graphs (DAGs) have directed edges (x, y) where x must come before y (e.g., scheduling problems).

```
G = {(a, b), (c, b), (a, c), (e, b), (b, d)}
```
- **In-degree:** The “in-degree” of a vertex v is the number of edges where second element of the ordered pair is v. For example, the "in-degree" for vertex b would be 3 since there are three edges that go into b: (a, b),(c, b),(e, b).


## Representations
1. **Adjacency Matrix:** In the adjacency matrix representation, a graph is represented in the form of a two-dimensional array. The size of the array is V x V, where V is the set of vertices.
2. **Adjacency List:** In the adjacency list representation, a graph is represented as an array of linked list. The index of the array represents a vertex and each element in its linked list represents the  vertices that form an edge with the vertex.

<table>
	<tr>
		<th>Comparison</th>
		<th>Best Representation</th>
	</tr>
	<tr>
		<td>Find (x,y) in graph</td>
		<td>Matrix</td>
	</tr>
	<tr>
		<td>Insert or delete edge</td>
		<td>Matrix</td>
	</tr>
	<tr>
		<td>Find degree of a vertex</td>
		<td>List</td>
	</tr>
	<tr>
		<td>Graph traversal</td>
		<td>List</td>
	</tr>
</table>

## Depth-First Search
Follows a path from the starting node to an ending node, then another path from start to end, etc. until all nodes are visited.
1.	Pick a node. If unvisited, mark it as visited and recur on all adjacent nodes.
2.	Repeat until all nodes are visited, or node to be searched is found.

```python
def dfs(grid, v):
	visited = set()
	if v in visited:
		return

	visited.add(v) 				    	# v = initial vertex 
	labeled as “discovered”
		for neighbor in grid[v]:		# neighbors = vertices 
			adjacent to v		  
			dfs(grid, neighbor)		    # recursion
```

https://leetcode.com/problems/number-of-islands/
https://leetcode.com/problems/friend-circles/
https://leetcode.com/problems/pacific-atlantic-water-flow/
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

### From Boundary
https://leetcode.com/problems/surrounded-regions/
https://leetcode.com/problems/number-of-enclaves/

### Time to reach all nodes
https://leetcode.com/problems/time-needed-to-inform-all-employees/

### Islands
https://leetcode.com/problems/number-of-closed-islands/
https://leetcode.com/problems/number-of-islands/
https://leetcode.com/problems/keys-and-rooms/
https://leetcode.com/problems/max-area-of-island/
https://leetcode.com/problems/flood-fill/
https://leetcode.com/problems/coloring-a-border/

### Cycle Find

## Breadth First-Search
Proceeds ‘level by level’, visiting all nodes on one level before moving on to the next.
1.	Pick a node, visit the adjacent unvisited vertex, mark as visited, and insert it in a queue.
2.	If no adjacent vertices left, remove first vertex from queue.
3.	Repeat 1 & 2 until queue is empty or node to be searched is found.

```python
def bfs(grid):
	visited = []
	queue = []

	visited.append(node)
	queue.append(node)
	while queue:						# while queue not empty
		v = queue.pop(0) 				# remove from front of queue
		for neighbor in grid[v]:		# search all adjacent vertices to v
			if neighbor not in visited:
				visited.append(neighbor)# mark neighbor as “visited”
				queue.append(neighbor) 	# add to back of queue
```

https://leetcode.com/problems/01-matrix/
https://leetcode.com/problems/as-far-from-land-as-possible/
https://leetcode.com/problems/rotting-oranges/
https://leetcode.com/problems/shortest-path-in-binary-matrix/

## Topological Sort
1. Compute "in-degree" for all vertices.
2. Traverse the vertex list, moving all vertices with an in-degree of 0 to a stack.
   1. For each element n in the stack, find each of its adjacent neighbors and reduce n's in-degree by 1.
   2. Remove n from the stack and from the vertex list.	
3. Repeat until stack is empty.

```python
def topological_sort(grid):
    res = []
    stack = [x for x in xrange(grid) if indeg[x] == 0]
    
    while stack:
        v = stack.pop()
        res.append(v)
        for n in neigh[v]:
            indeg[n] -= 1
            if indeg[n] == 0:
                stack.append(n)
        neigh.pop(v)
    
    return res if len(res) == grid else []
```


## Dijkstras and Bellman Ford
1. Initialize vertex "s" by marking as visited.
2. For vertices not visited, set their intial distance to grid[1][s]
3. While there are unknown vertices:
   1. Choose a vertex w where the distance[w] is a minimum
   2. Add w to the visited set
   3. For each unknown vertex v: distance[v] = min(distance[v], distance[w] + grid[w,v])
   
```python
def dijkstras(grid):
	visited = []
	distance = []
	parent = []
	
	visited[1] = True	# start with vertex 1
	distance[1] = 0
	parent[1] = 0		# no parent for first element

	# distance from initial node
	for i in range(2, vertices):
		if grid[1][i] > 0:
			distance[i] = grid[1][i]
	
	for x in range(1, vertices):

		# choose lowest cost element in the available set
		min_v = vertices + 1
		min_cost = 99

		for i in range(1, vertices):
			# find minimal element to add
			if not visited[i]:
				if distance[i] < min_cost:	# candidate found
					min_cost = distance[i]
					min_v = i
		
		visited[min_v] = True
		for i in range(1, vertices):
			if not visited[i]:
				if distance[min_v] + grid[min_v][i] < distance[i]:
					parent[i] = min_v
				distance[i] = min(distance[i], distance[min_v] + cost[min_v][i])

```

https://leetcode.com/problems/network-delay-time/
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
https://leetcode.com/problems/cheapest-flights-within-k-stops/

## All pairs shortest path problem: Floyd's

```python
def floyd(grid):

	A = [[0 for _ in range(grid[0])] for _ in range(grid)]
	for i in range(1, vertices):
		for j in range(1, vertices):
			A[i][j] = grid[i][j]

	for k in range(1, vertices):
		for i in range(1, vertices):
			for j in range(1, vertices):
				if A[i][k] + A[k][j] < A[i][j]:
					A[i][j] = A[i][k] + A[k][j]
					parent[i][j] = k
```

## Prim's
Prim’s algorithm is essentially the Dijkstra algorithm applied to spanning trees rather than just shortest paths.
```python
def prim(grid):
	V = set()
	U = set()

	while V:
		min = 99
		edge = (999, 999, 999)
		for x in grid:
			if U.find(x) and V.find(x):
				if x < min:
					edge = x
					min = edge
		U.insert(edge)
		V.insert(edge)
```
## Kruskal's
1. Initialize disjoint set and priority queue.
2. Order the edges, lowest weight to highest weight. 
3. Initialize minimal spanning tree as an empty list of edges. To keep up with which vertices are already in the minimal spanning tree and which are not.
   
```python
def kruskal(grid):
	s = set(grid)
	pq = prirorityqueue()
	min_span_tree = []

	while pq and len(min_space_tree) != vertices - 1:
		edge = pq.pop()

		u = s.find(edge)
		v = s.find(edge)

		if u != v:
			min_span_tree.append(edge)
			s.add(u)
			s.add(v)
		
```

https://leetcode.com/problems/optimize-water-distribution-in-a-village/

## Connectivity
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

## Strongly Connected Components: Tarjan's Algorithm 
https://leetcode.com/problems/critical-connections-in-a-network/

## Coloring
https://leetcode.com/problems/possible-bipartition/
https://leetcode.com/problems/is-graph-bipartite/

## Hierholzer's algorithm for Eulerian circuits
https://leetcode.com/problems/reconstruct-itinerary/

## A* search
https://leetcode.com/problems/sliding-puzzle/