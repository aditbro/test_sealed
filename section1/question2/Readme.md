## Complexity Analysis

### Time Complexity
There are 2 stages in the program, parsing the input into graph and finding the optimal route. the parsing function itself has the complexity of O(V + E) where V is the number of vertices and E is the number of edge, since the function iterate all of the vertices and edge list (assuming dictionary access is O(1)). The complexity of the pathfinding function is O(E) because all edges (that's connected to the initial point) will be visited exactly once by the function regardless of the number of vertices. So the overall complexity of the solution is O(V + E).

### Memory Complexity
The program uses extra space as much as the number of Vertices and Edges in the input. The vertices will become the graph nodes and the edges will be a pointer to the vertices location. So overall the memory complexity is O(V + E)

## Case if the graph is cyclic
To handle cycle