# Leetcode 277. Find the Celebrity
# Medium 12/31/20

# Problem link from GeeksForGeeks:
# http://www.practice.geeksforgeeks.org/problem-page.php?pid=700253

# Suppose you are at a party with $n$ people (labeled from $0$ to $n - 1$) and among them, there may exist one celebrity. The definition of a celebrity is that all the other $n - 1$ people know him/her but he/she does not know any of them. Your task is to find the stranger (celebrity) in party.

# Input:

# The first line of input contains an element T denoting the No of test cases. Then T test cases follow. Each test case consist of 2 lines. The first line of each test case contains a number denoting the size of the matrix M. Then in the next line are space separated values of the matrix M.

# Output:

# For each test case output will be the id of the celebrity if present (0 based index). Else -1 will be printed.

# Graph

# Each node denotes a person, and edge(A, B) means A knows B. So the celebrity should be the node with 0
# out-degree and n−1

# in-degree. Also, in the graph, there is only possible one celebrity node. Therefore, we can find a 0-out-degree node first. If there is no such node, there is no celebrity neither. Then, we check if this node is celebrity, if not there is no celebrity node in the graph. Other nodes cannot be celebrity because at least 0-out-degree node does not know him/her.
# Celebrity Candidate

# However, the time complexity to find the 0-out-degree node is O(n2). 
# Taking a step back, we can find the celebrity candidate, we note that:

#     If One knows somebody else, then he cannot be a celebrity.
#     If somebody doesn’t know A, then A cannot be a celebrity.


def getId(arr, n):
    #Code here
    i = 0
    j = n - 1
    
    # Find the celebrity candidate
    while i < j:
        if arr[i][j] == 1:
            # i knows j ==> i cannot be a celebrity
            i += 1
        else:
            # i doesn't know j ==> j cannot be a celebrity
            j -= 1
            
    # Now i = j is the person who is possibly a celebrity
    # Check if candidate (j) is a celebrity by checking its relationships with all other people
    for i in xrange(n):
        # if i == j, skip; Otherwise, check the celebrity condition i is known by j but i doesn't know j.
        # If it is true, then continue to check next j, or return false
        if i != j and (arr[i][j] == 0 or arr[j][i] == 1):
            return -1
    return i    

# Edge check of arr[i][j] is an O(1) operation.
# T: O(a)
# S: O(a)