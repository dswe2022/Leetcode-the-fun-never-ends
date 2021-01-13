# Leetcode 56. Merge Intervals
# Medium 1/2/21

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



# Solution 1 (Best optimal solution)
# Intuition

# If we sort the intervals by their start value, then each set of intervals that can be merged will appear as a contiguous "run" in the sorted list.

# Algorithm

# First, we sort the list as described. Then, we insert the first interval into our merged list and continue considering each interval in turn as follows: 
# If the current interval begins after the previous interval ends, then they do not overlap and we can append the current interval to merged. Otherwise, they do overlap, 
# and we merge them by updating the end of the previous interval if it is less than the end of the current interval.

# A simple proof by contradiction shows that this algorithm always produces the correct answer. First, suppose that the algorithm at some point fails to merge two intervals that should be
#  merged. This would imply that there exists some triple of indices iii, jjj, and kkk in a list of intervals ints\text{ints}ints such that i<j<ki < j < ki<j<k and (ints[i]\text{ints[i]}ints[i], 
# ints[k]\text{ints[k]}ints[k]) can be merged, but neither (ints[i]\text{ints[i]}ints[i], ints[j]\text{ints[j]}ints[j]) nor (ints[j]\text{ints[j]}ints[j], ints[k]\text{ints[k]}ints[k]) can be merged. 
# From this scenario follow several inequalities:

# ints[i].end<ints[j].startints[j].end<ints[k].startints[i].end≥ints[k].start \begin{aligned} \text{ints[i].end} < \text{ints[j].start} \\ \text{ints[j].end} < \text{ints[k].start} \\ \text{ints[i].end}
#  \geq \text{ints[k].start} \\ \end{aligned} ints[i].end<ints[j].startints[j].end<ints[k].startints[i].end≥ints[k].start​

# We can chain these inequalities (along with the following inequality, implied by the well-formedness of the intervals: 
# ints[j].start≤ints[j].end\text{ints[j].start} \leq \text{ints[j].end}ints[j].start≤ints[j].end) to demonstrate a contradiction:

# ints[i].end<ints[j].start≤ints[j].end<ints[k].startints[i].end≥ints[k].start \begin{aligned} \text{ints[i].end} < \text{ints[j].start} \leq \text{ints[j].end} 
# < \text{ints[k].start} \\ \text{ints[i].end} \geq \text{ints[k].start} \end{aligned} ints[i].end<ints[j].start≤ints[j].end<ints[k].startints[i].end≥ints[k].start​

# Therefore, all mergeable intervals must occur in a contiguous run of the sorted list.



class Solution:   
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.

            # SUPER KEY STEP!! you look at each pair and look at the second part of the pair. 
            # If the next pair's second index is less than the current one's second index than, we 
            # can say the initial boundary begins on that interval number.
            if not merged or merged[-1][1] < interval[0]: 
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


# Time complexity : O(nlog⁡n)O(n\log{}n)O(nlogn)
# Other than the sort invocation, we do a simple linear scan of the list, so the runtime is dominated by the O(nlog⁡n)O(n\log{}n)O(nlogn) complexity of sorting.
# Space complexity : O(log⁡N)O(\log N)O(logN) (or O(n)O(n)O(n))
# If we can sort intervals in place, we do not need more than constant additional space, although the sorting itself takes O(log⁡n)O(\log n)O(logn) space. Otherwise, we must allocate linear space to store a copy of intervals and sort that.













# Solution 2: (non-optimal solution, certain issues)

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

 

# Constraints:

#     1 <= intervals.length <= 104
#     intervals[i].length == 2
#     0 <= starti <= endi <= 104



# Approach 1: Connected Components

# Intuition

# If we draw a graph (with intervals as nodes) that contains undirected edges between all pairs of intervals that overlap, 
# then all intervals in each connected component of the graph can be merged into a single interval.

# Algorithm

# With the above intuition in mind, we can represent the graph as an adjacency list, inserting directed edges in both directions 
# to simulate undirected edges. Then, to determine which connected component each node is it, we perform graph traversals from arbitrary 
# unvisited nodes until all nodes have been visited. To do this efficiently, we store visited nodes in a Set, allowing for constant time 
# containment checks and insertion. Finally, we consider each connected component, merging all of its intervals by constructing a new 
# Interval with start equal to the minimum start among them and end equal to the maximum end.

# This algorithm is correct simply because it is basically the brute force solution. We compare every interval to every other interval, 
# so we know exactly which intervals overlap. The reason for the connected component search is that two intervals may not directly overlap,
#  but might overlap indirectly via a third interval. See the example below to see this more clearly.

# Components Example

# Although (1, 5) and (6, 10) do not directly overlap, either would overlap with the other if first merged with (4, 7). There are two connected 
# components, so if we merge their nodes, we expect to get the following two merged intervals:

# (1, 10), (15, 20)



class Solution:
    def overlap(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]

    # generate graph where there is an undirected edge between intervals u
    # and v iff u and v overlap.
    def build_graph(self, intervals):
        graph = collections.defaultdict(list)
        for i, interval_i in enumerate(intervals):
            for j in range(i+1, len(intervals)):
                if self.overlap(interval_i, intervals[j]):
                    graph[tuple(interval_i)].append(intervals[j])
                    graph[tuple(intervals[j])].append(interval_i)
        return graph

    # merges all of the nodes in this connected component into one interval.
    def merge_nodes(self, nodes):
        min_start = min(node[0] for node in nodes)
        max_end = max(node[1] for node in nodes)
        return [min_start, max_end]
    
    # gets the connected components of the interval overlap graph.
    def get_components(self, graph, intervals):
        visited = set()
        comp_number = 0
        nodes_in_comp = collections.defaultdict(list)
        def mark_component_dfs(start):
            stack = [start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])
        # mark all nodes in the same connected component with the same integer.
        for interval in intervals:
            if tuple(interval) not in visited:
                mark_component_dfs(interval)
                comp_number += 1
        return nodes_in_comp, comp_number
    
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        graph = self.build_graph(intervals)
        nodes_in_comp, number_of_comps = self.get_components(graph, intervals)

        # all intervals in each connected component must be merged.
        return [self.merge_nodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]


# Complexity Analysis
# Time complexity : O(n2)O(n^2)O(n2)
# Building the graph costs O(V+E)=O(V)+O(E)=O(n)+O(n2)=O(n2)O(V + E) = O(V) + O(E) = O(n) + O(n^2) = O(n^2)O(V+E)=O(V)+O(E)=O(n)+O(n2)=O(n2) time, as in the worst case all
#  intervals are mutually overlapping. Traversing the graph has the same cost (although it might appear higher at first) because our visited set guarantees that each node will
#  be visited exactly once. Finally, because each node is part of exactly one component, the merge step costs O(V)=O(n)O(V) = O(n)O(V)=O(n) time. This all adds up as follows:
# O(n2)+O(n2)+O(n)=O(n2) O(n^2) + O(n^2) + O(n) = O(n^2) O(n2)+O(n2)+O(n)=O(n2)
# Space complexity : O(n2)O(n^2)O(n2)
# As previously mentioned, in the worst case, all intervals are mutually overlapping, so there will be an edge for every pair of intervals. Therefore, the memory footprint is quadratic in the input size.


