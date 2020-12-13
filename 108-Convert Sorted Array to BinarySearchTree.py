# Leetcode 108 Convert Sorted Array to Binary Search Tree
# Easy 12/13/20 

# Given the sorted array: [-10,-3, 0, 5, 9]
# One possible answer is [0,-3, 9, -10, null, 5]
# which represents the following height balanced BST:


class Solution:
    def sortedArrayToBST(self, nums):
        def buildBST(l,r):
            if l>r:
                return None
            m = (l+r)//2
            root = TreeNode(nums[m])
            root.left = buildBST(l, m-1)
            root.right = buildBST(m+1, r)
            return root

        return buildBST(0, len(nums) - 1)

# Time: O(a)
# Space: O(log(a))

