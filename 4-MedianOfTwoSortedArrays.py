# 4. Median of Two Sorted Arrays
# Hard 1/15/21

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# Follow up: The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Example 3:

# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000

# Example 4:

# Input: nums1 = [], nums2 = [1]
# Output: 1.00000

# Example 5:

# Input: nums1 = [2], nums2 = []
# Output: 2.00000

 

# Constraints:

#     nums1.length == m
#     nums2.length == n
#     0 <= m <= 1000
#     0 <= n <= 1000
#     1 <= m + n <= 2000
#     -106 <= nums1[i], nums2[i] <= 106


# Solution 1 60 ms

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        data = sorted(nums1 + nums2)
        mid = len(data) // 2
        return (data[mid] + data[-mid-1:][0]) / 2

# Solution 2 64 ms
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        length=len(nums1)
        mid1=(length-1)//2
        mid2=length//2
        if length%2==0:
            return (nums1[mid2]+nums1[mid2-1])/2
        return nums1[mid1]



# Solution 3 75 ms
class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        m,n = len(a), len(b)
        if m > n:
            a, b, m, n = b,a,n,m
        i=0
        j=0
        imin,imax = 0, m
        while imin <= imax:
            i = int((imin+imax)/2)
            j = int(((m + n + 1)/2) - i)
            
            if (i < m and j > 0 and b[j-1] > a[i]):
                imin = i + 1
            elif (i > 0 and j < n  and a[i-1] > b[j]):
                imax = i -1
            else:
                if i == 0: max_of_left=b[j -1]
                elif j == 0: max_of_left=a[i-1]
                else: 
                    max_of_left = max(a[i-1], b[j-1])
                break

        if (m+n)%2 == 1:
            return max_of_left

        if i == m: return (max_of_left + b[j])/2.0
        if j == n: return (max_of_left + a[i])/2.0
        
        return (max_of_left + min(a[i],b[j]))/2.0





# Solution 4

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        x=len(nums)
        if x%2==1:
            return nums[x//2]
        else:
            return (nums[(x-1)//2]+nums[x//2])/2

# Not desired time complexity
# T: O(alog(a+b))
# S: O(1)


