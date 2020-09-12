
# Union Find
https://leetcode.com/problems/friend-circles/
https://leetcode.com/problems/redundant-connection/
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
https://leetcode.com/problems/number-of-operations-to-make-network-connected/
https://leetcode.com/problems/satisfiability-of-equality-equations/
https://leetcode.com/problems/accounts-merge/
https://leetcode.com/problems/connecting-cities-with-minimum-cost/

# Depth-First Search
Follows a path from the starting node to an ending node, then another path from start to end, etc. until all nodes are visited.
1.	Pick a node. If unvisited, mark it as visited and recur on all adjacent nodes.
2.	Repeat until all nodes are visited, or node to be searched is found.
<pre>
<code>
visited = set()
def DFS (grid, v):
	if v in visited:
		return

visited.add(v) 				    # v = initial vertex 
labeled as “discovered”
	for neighbor in grid[v]:	# neighbors = vertices 
adjacent to v		  
DFS (grid, neighbor)		    # recursion
</code>
</pre>

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
https://leetcode.com/problems/01-matrix/
https://leetcode.com/problems/as-far-from-land-as-possible/
https://leetcode.com/problems/rotting-oranges/
https://leetcode.com/problems/shortest-path-in-binary-matrix/

## Coloring
https://leetcode.com/problems/possible-bipartition/
https://leetcode.com/problems/is-graph-bipartite/

## Connectivity
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

## Topological Sort
https://leetcode.com/problems/course-schedule-ii/

## Dijkstras and Bellman Ford
https://leetcode.com/problems/network-delay-time/
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
https://leetcode.com/problems/cheapest-flights-within-k-stops/
