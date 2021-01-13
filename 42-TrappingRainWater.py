# Leetcode 42. Trapping Rain Water
# Hard 1/12/21

# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

 

# Constraints:

#     n == height.length
#     0 <= n <= 3 * 104
#     0 <= height[i] <= 105


# Solution 1 Two pointer way


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<= 2:
            return 0

        ans = 0

        #using two pointers i and j on indices 1 and n-1
        i = 1
        j = len(height) - 1

        #initialising leftmax to the leftmost bar and rightmax to the rightmost bar
        lmax = height[0]
        rmax = height[-1]

        while i <=j:
            # check lmax and rmax for current i, j positions
            if height[i] > lmax:
                lmax = height[i]
            if height[j] > rmax:
                rmax = height[j]

            #fill water upto lmax level for index i and move i to the right
            if lmax <= rmax:
                ans += lmax - height[i]
                i += 1

            #fill water upto rmax level for index j and move j to the left
            else:
                ans += rmax - height[j]
                j -= 1

        return ans

# T: O(a)
# S: O(1)





# Solution 2 

class Solution:
    def trap(self, height: List[int]) -> int:
        #The total water is decided by left_max and right_max: these 2 arrays
        #But, need to minus the building in the building array
        
        if len(height) < 3: # if there are 2 or less element, there is no water collected
            return 0
        
        left_max = [None] * len(height) # check from leftside
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i])
            
        right_max = [None] * len(height) # check from right side
        right_max[-1] = height[-1]
        for i in range(-2, -len(height) - 1, -1):
            right_max[i] = max(right_max[i+1], height[i])
            
        total_water = [] # there is no 2 sides accounted in total water
        for i in range(1, len(height) - 1):
            total_water.append(min(left_max[i], right_max[i]) - height[i])
        return sum(total_water)

# T: O(a)
# S: O(1)