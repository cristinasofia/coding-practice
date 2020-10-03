# Graphs

## Union Find
https://leetcode.com/problems/friend-circles/
https://leetcode.com/problems/redundant-connection/
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
https://leetcode.com/problems/number-of-operations-to-make-network-connected/
https://leetcode.com/problems/satisfiability-of-equality-equations/
https://leetcode.com/problems/accounts-merge/
https://leetcode.com/problems/connecting-cities-with-minimum-cost/

## Depth-First Search
Follows a path from the starting node to an ending node, then another path from start to end, etc. until all nodes are visited.
1.	Pick a node. If unvisited, mark it as visited and recur on all adjacent nodes.
2.	Repeat until all nodes are visited, or node to be searched is found.

```python
visited = set()
def dfs(grid, v):
	if v in visited:
		return

visited.add(v) 				    # v = initial vertex 
labeled as “discovered”
	for neighbor in grid[v]:	# neighbors = vertices 
		adjacent to v		  
		dfs(grid, neighbor)		    # recursion
```

https://leetcode.com/problems/number-of-islands/
https://leetcode.com/problems/friend-circles/
https://leetcode.com/problems/pacific-atlantic-water-flow/
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

## From Boundary
https://leetcode.com/problems/surrounded-regions/
https://leetcode.com/problems/number-of-enclaves/

## Shortest Time
https://leetcode.com/problems/time-needed-to-inform-all-employees/

## Islands
https://leetcode.com/problems/number-of-closed-islands/
https://leetcode.com/problems/number-of-islands/
https://leetcode.com/problems/keys-and-rooms/
https://leetcode.com/problems/max-area-of-island/
https://leetcode.com/problems/flood-fill/
https://leetcode.com/problems/coloring-a-border/

## Hash
https://leetcode.com/problems/employee-importance/
https://leetcode.com/problems/find-the-town-judge/

## Cycle Find

# BFS
Proceeds ‘level by level’, visiting all nodes on one level before moving on to the next.
1.	Pick a node, visit the adjacent unvisited vertex, mark as visited, and insert it in a queue.
2.	If no adjacent vertices left, remove first vertex from queue.
3.	Repeat 1 & 2 until queue is empty or node to be searched is found.

```python
visited = []
queue = []

visited.append(node)
queue.append(node)
while queue:					# while queue not empty
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
https://leetcode.com/problems/course-schedule-ii/

## Dijkstras and Bellman Ford
https://leetcode.com/problems/network-delay-time/
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
https://leetcode.com/problems/cheapest-flights-within-k-stops/

## Connectivity
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

## Strongly Connected Components: Tarjan's Algorithm 
https://leetcode.com/problems/critical-connections-in-a-network/

## Coloring
https://leetcode.com/problems/possible-bipartition/
https://leetcode.com/problems/is-graph-bipartite/

## Prim's and Kruskal's algorithm
https://leetcode.com/problems/optimize-water-distribution-in-a-village/

## Hierholzer's algorithm for Eulerian circuits
https://leetcode.com/problems/reconstruct-itinerary/

## A* search
https://leetcode.com/problems/sliding-puzzle/