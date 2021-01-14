# Leetcode 1192. Critical Connections in a Network
# Hard 1/14/21

# There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

# A critical connection is a connection that, if removed, will make some server unable to reach some other server.

# Return all critical connections in the network in any order.

 

# Example 1:

# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.

 

# Constraints:

#     1 <= n <= 10^5
#     n-1 <= connections.length <= 10^5
#     connections[i][0] != connections[i][1]
#     There are no repeated connections.



# Solution 1: DFS with tarjan's algorithm. O(n) time and O(n) space complexity
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(current_rank, prev_vertex, current_vertex):
            # visit the current node
            visited.add(current_vertex)
            # update the lowest possible node order that can be gone from this current node
            # at first it's the same as discovery time of the node
            lowest_rank[current_vertex] = current_rank
            # now check on the next virtices that are neighbor of the current vertex
            for next_vertex in graph[current_vertex]:
                # if it is not the same as the previous vertex from where we have come 
                # to current vertex while DFS
                if next_vertex != prev_vertex:
                    # if the vertex not in visited, do dfs on it
                    # discovery time/rank would be 1 more than the current vertex
                    if next_vertex not in visited:
                        dfs(current_rank+1, current_vertex, next_vertex)
                    # update the rank with the lowest ordered node that can be possible 
                    # to go from this current node
                    # check the minimum and update if applicable
                    lowest_rank[current_vertex] = min(lowest_rank[current_vertex], lowest_rank[next_vertex])
                    # print(next_vertex, current_vertex, lowest_rank[next_vertex], lowest_rank[current_vertex])
                    # now if the current rank (discovery time) of the current_vertex is less 
                    # than this neighbor vertex means there is no connection for this neighbor 
                    # vertex to another earlier discovered vertex 
                    # without going through this current vertex. So this is a critical connection
                    # print(current_vertex, next_vertex, current_rank)
                    if lowest_rank[next_vertex] > current_rank:
                        result.append([current_vertex, next_vertex])
        # build the graph            
        graph = defaultdict(list)
        for x,y in connections:
            graph[x].append(y)
            graph[y].append(x)
        # print(graph)
            
        # hashset for track the visited nodes
        visited = set()
        # the first order while DFS, you may think of it as discovery time which starts from 0
        current_rank = 0
        # will store the lowest order possible to go from the current node
        # at first the lowest order is the same as discovery time of the node while dfs
        lowest_rank = [-1 for i in range(n)]
        
        # DFS starts from node number 0 (note that here nodes are numbered from 0 to n-1)
        # it's discovery time/ rank is also 0
        current_vertex = 0
        prev_vertex = -1 # a dummy placeholder for previous of starting node.
        result = [] # will store the reult edges
        # start dfs on the current vertex. Also provide the rank of it and it's previous vertex
        dfs(current_rank, prev_vertex, current_vertex)
        # print(result)
        return result
        
        