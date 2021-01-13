# Leetcode 210. Course Schedule II
# Medium 12/31/20

# There are a total of n courses you have to take labelled from 0 to n - 1.

# Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

# Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

# If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]

 

# Constraints:

#     1 <= numCourses <= 2000
#     0 <= prerequisites.length <= numCourses * (numCourses - 1)
#     prerequisites[i].length == 2
#     0 <= ai, bi < numCourses
#     ai != bi
#     All the pairs [ai, bi] are distinct.



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {i : [] for i in range(numCourses)}
        indegree = {i : 0 for i in range(numCourses)}
        
        for item in prerequisites:
            indegree[item[0]] += 1
            graph[item[1]].append(item[0])
            
        q = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                
        res = []
        while (len(q) > 0):
            tmp = q.pop(0)
            res.append(tmp)
            
            for neighbor in graph[tmp]:
                if indegree[neighbor] > 0:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)
        
        return res if len(res) == numCourses else []


# T: O(a*b), a is length of q and b is number of neighors in graph.
# S: O(c), c is graph space.
