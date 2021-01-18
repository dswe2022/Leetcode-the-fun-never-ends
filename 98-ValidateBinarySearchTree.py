# Leetcode 98. Validate Binary Search Tree
# Medium 1/12/21

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.

 

# Example 1:

# Input: root = [2,1,3]
# Output: true

# Example 2:

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

 

# Constraints:

#     The number of nodes in the tree is in the range [1, 104].
#     -231 <= Node.val <= 231 - 1



# Solution Stack based

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        curr = root
        stack = []
        inorderList = []
        while (curr is not None or len(stack) != 0):
            while (curr is not None):
                stack.append(curr)
                curr = curr.left
            curr = stack.pop(len(stack) -1)
            curr_len = len(inorderList)
            if (curr_len > 0):
                if (inorderList[curr_len-1] >= curr.val):
                    return False
            inorderList.append(curr.val)
            curr = curr.right
        return True


# Solution Recursion based

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        min_val = -math.inf
        max_val = math.inf 
        
        if not root:
            return True
        
        #all conditions met?
        #1. root.val > min value
        #2. root.val < max value
        #3. left subtree's val is lesser than its root's value?
        #4. right subtree's val is greater than its root's value?
        
        def helper(root, low, high):
            if not root:
                return True
            return root.val > low and root.val < high and \
                   helper(root.left, low, root.val) and helper(root.right, root.val, high)
        
        return helper(root, min_val, max_val)