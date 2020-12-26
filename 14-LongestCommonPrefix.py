# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string ""


# 1) Use built-inall() and startswith() functions. It first finds the shortest word in 
# the input array, then it iterates each character of the shortest word to find out whether
# the character is common to the rest of words.
# O(S) time where S is the total number of characters for all words in the array, O(1) space;


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_pre = ""
        if not strs: return longest_pre
        shortest_str = min(strs, key=len)
        for i in range(len(shortest_str)):
            if all([x.startswith(shortest_str[:i+1]) for x in strs]):
                longest_pre = shortest_str[:i+1]
            else:
                break
        return longest_pre



# 2) Use enumerate() and nested for loop to check each char for each word. O(S)
# time where S is the total number of characters for all words in the array, O(1) space

class Solution:
    def longestCommonPrefix(self, strs):
    if not strs:
        return ""
    shortest_str = min(strs,key=len)
    for i, char in enumerate(shortest_str):
        for other in strs:
            if other[i] != char:
                return shortest_str[:i]
    return shortest_str




# 3) Use zip() andset(), if the length of set greater than 1, return the current longest common prefix.
# enumerate(zip(*strs)) returns index and tuple of characters from each word. To note here set() to 
# convert the list to set has time complexity of O(N) where N is the number of words in the array. Consider the for loop, overall time complexity is 
# still O(S) where S is the total number of characters for all words in the array, O(1) space;


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        for i, letter_group in enumerate(zip(*strs)):
            # ["flower","flow","flight"]
            # print(i,letter_group,set(letter_group))
            # 0 ('f', 'f', 'f') {'f'}
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)


# 4) Use zip() andset() without enumerate(), zip(*str) returns a zip object where each tuple has characters 
# with the corresponding index from each word. 
# Similarly, O(S) time where S is the total number of characters for all words in the array, O(1) space;          

def longestCommonPrefix(self, strs):
    letter_groups, longest_pre = zip(*strs), ""
    # print(letter_groups, longest_pre)
    # [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')] 
    for letter_group in letter_groups:
        if len(set(letter_group)) > 1: break
        longest_pre += letter_group[0]
    return longest_pre


# 5) Use min() and max() on array of strings. These two functions return the first and last words of
# the sorted input array (lexicographically). If the character in min_s is in max_s at the corresponding 
# index, the character must be in the remaining
# words at the corresponding index as well. This is because the input array of words have already been sorted;

def longestCommonPrefix(self, strs):
    if not strs:
        return ""
    min_s = min(strs)
    max_s = max(strs)
    if not min_s:
        return ""
    for i in range(len(min_s)):
        if max_s[i] != min_s[i]:
            return max_s[:i]
    return min_s[:]


# 6) Use sorted() on the array of strings
# and compare first and last words of sorted array index by index. It is the variant of #5;
def longestCommonPrefix(self, strs):
    longest_pre = []
    if strs and len(strs) > 0:
        strs = sorted(strs)
        # e.g. before sort: ["flower","flow","flight","fake"]
        # after sort: ['fake', 'flight', 'flow', 'flower']
        first, last = strs[0], strs[-1]
        for i in range(len(first)):
            if len(last) > i and last[i] == first[i]:
                longest_pre.append(last[i])
            else:
                return "".join(longest_pre)
    return "".join(longest_pre)
view raw


# 7) Use find(), start with the first word in the input array as the longest prefix. 
# Horizontal scanning where the outer loop is for each individual remaining words, inner 
# loop for each individual character of the word, decrement the length of the 
# longest prefix. O(S) time where S is the total number of characters for all words in the array, O(1) space;

def longestCommonPrefix(self, strs):
    if not strs: return ""
    longest_pre = strs[0]
    for i in range(1,len(strs)):
        while(strs[i].find(longest_pre)!=0):
            longest_pre = longest_pre[:-1]
            if len(longest_pre) == 0: return ""
    return longest_pre



#8) Vertical scanning where the outer loop is for each character of the first word 
# in the input array, inner loop for each individual words. Increment the index of 
# the first word as the longest common prefix. It is more optimized compared to #7 
# in dealing with the case where there is a very short word at end of the input array.
# O(S) time where S is the total number of characters for all words in the array, O(1) space;

def longestCommonPrefix(self, strs):
    if not strs: return ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1,len(strs)):
            if i == len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]
    return strs[0]


#9) Divide and conquer, the intuition is LCP(W1,W2,W3...Wn) = LCP(LCP(W1,W2...Wk-1),LCP(Wk,Wk+1...Wn)) 
# Hence we can recursively divide the problem of finding LCP of an input array of words into 2 sub-problems of
# finding LCP on sub-components. commonPrefix() returns the common prefix of two sub-components. We recursively 
# divide and combine from a basic case to make up the final longest common prefix. O(S) time where S is 
# the total number of characters for all words in the array, O(Mlog(N)) space where N is the number of words 
# in the array,
# M is the largest length of a word as we make log(N) recursive call and each call requires O(M) space;

def longestCommonPrefix(self, strs):
    def commonPrefix(left,right):
        min_len = min(len(left), len(right))
        for i in range(min_len):
            if left[i] != right[i]:
                return left[:i]
        return left[:min_len]

    def find_longestCommonPrefix(strs, left_index, right_index):
        if left_index == right_index:
            return strs[left_index]
        # recursive call
        else:
            mid_index = (left_index + right_index)//2
            lcpLeft = find_longestCommonPrefix(strs,left_index, mid_index)
            lcpRight = find_longestCommonPrefix(strs,mid_index+1,right_index)
            return commonPrefix(lcpLeft,lcpRight)

    if not strs: return ""
    return find_longestCommonPrefix(strs, 0, len(strs)-1)


#10) Binary search on the length of the prefix on the first word of the input array. 
# isCommonPrefix() function test whether a given length of the first word produces a common 
# prefix for all words in the array. O(Slog(M)) time where S is the total number of characters
# for all words in the array, M is the length of the longest word in the array as we iterate log(M) times 
# for the binary search on prefix length. For each time,
# we perform comparisons on N words of maximum M characters. Hence O(MNlog(M)) = O(Slog(M)) time, O(1) space;

def longestCommonPrefix(self, strs):
    def isCommonPrefix(strs, length):
        # has to put 0 in the strs index
        strl = strs[0][:length]
        print(strl)
        for i in range(1,len(strs)):
            if not strs[i].startswith(strl):
                return False
        return True

    if not strs: return ""
    minLen = len(min(strs, key=len))
    low, high = 1, minLen
    # the binary search on the length of prefix on the first word
    while(low<=high):
        mid = (low+high) // 2
        if (isCommonPrefix(strs, mid)):
            low = mid + 1
        else:
            high = mid - 1
    return strs[0][:high]




# Solution 11
# With all the efforts above, interestingly, Python has a built-in commonprefix()function
# to solve the problem in single-line:

return os.path.commonprefix(strs)