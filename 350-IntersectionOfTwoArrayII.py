# Leetcode 350 Missing Number
# Easy 12/18/20 
# Given two arrays, write a function to compute their intersection.


# Solution 1
def intersect(num1,num2):
    nums1.sort()
    nums2.sort()
    L1 = 0
    L2 = 0
    N1 = len(nums1)
    N2 = len(nums2)
    res = []
    
    while L1 != N1 and L2 != N2:
        if nums1[L1] == nums2[L2]:
            res.append(nums1[L1])
            L1 += 1
            L2 += 1 
        elif nums1[L1] < num2[L2]:
            L1 += 1
        else:
            L2 +=1

    return res


# Time: O(a*log(a))
# Space: O(1)



# Solution 2
import Counter from collection

def intersect(nums1, nums2):
    count1 = collections.Counter(nums1)
    count2 = collections.Counter(nums2)
    res = []
    for k,v in count1.items():
        if k in count2:
            res += [k]*min(v,count2[k])
    return res


# Time: O(a)
# Space: O(a)

