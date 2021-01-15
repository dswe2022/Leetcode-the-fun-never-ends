# Leetcode 895. Maximum Frequency Stack
# Hard 1/14/21

# Implement FreqStack, a class which simulates the operation of a stack-like data structure.

# FreqStack has two functions:

#     push(int x), which pushes an integer x onto the stack.
#     pop(), which removes and returns the most frequent element in the stack.
#         If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.

 

# Example 1:

# Input: 
# ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
# [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
# Output: [null,null,null,null,null,null,null,5,7,5,4]
# Explanation:
# After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

# pop() -> returns 5, as 5 is the most frequent.
# The stack becomes [5,7,5,7,4].

# pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
# The stack becomes [5,7,5,4].

# pop() -> returns 5.
# The stack becomes [5,7,4].

# pop() -> returns 4.
# The stack becomes [5,7].

 

# Note:

#     Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
#     It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
#     The total number of FreqStack.push calls will not exceed 10000 in a single test case.
#     The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
#     The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()



# Solution 1


# Approach 1: Stack of Stacks

# Intuition

# Evidently, we care about the frequency of an element. Let freq be a Map from xxx to the number of occurrences of xxx.

# Also, we (probably) care about maxfreq, the current maximum frequency of any element in the stack. This is clear because we must pop the element with the maximum frequency.

# The main question then becomes: among elements with the same (maximum) frequency, how do we know which element is most recent? We can use a stack to query this information: the top of the stack is the most recent.

# To this end, let group be a map from frequency to a stack of elements with that frequency. We now have all the required components to implement FreqStack.

# Algorithm

# Actually, as an implementation level detail, if x has frequency f, then we'll have x in all group[i] (i <= f), not just the top. This is because each group[i] will store information related to the ith copy of x.

# Afterwards, our goal is just to maintain freq, group, and maxfreq as described above.


class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x: int) -> None:
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self) -> int:
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return x



# Complexity Analysis

#     Time Complexity: O(1) for both push and pop operations.

#     Space Complexity: O(N), where N is the number of elements in the FreqStack. 





# Solution 2 Binary Search Tree 
# The idea here is to maintain 2 hash maps. The first hash map maps from value x to the tuple (freq(x), last_occurence(x), x). The second hash map is the inverse of the first one, i.e. (freq(x), last_occurence(x), x).

# We implement the first hash map as a Sorted Dict. A Sorted Dict is a Binary Search Tree with ordered keys. That means we can add, remove and get maximum-key item all in O(logN).


from sortedcontainers import SortedDict, SortedList

class FreqStack:

    def __init__(self):
        self.occurences = defaultdict(list) #ocucrences[i] = [1, 5, 6] means arr[1] = arr[5] = arr[6] = i
        self.val_to_key = {} # val -> (freq, last_oc, val)
        self.key_to_val = SortedDict() #(freq, last_oc, val) -> val
        self.keys = SortedList()
        self.i = 0
    def push(self, x: int) -> None:
        if x not in self.val_to_key:
            self.val_to_key[x] = (1, self.i, x)
            self.key_to_val[(1, self.i, x)] = x
            self.keys.add((1, self.i, x))
        else:
            oldfreq, oldlast_oc, _ = self.val_to_key[x]
            del self.key_to_val[(oldfreq, oldlast_oc, x)]
            self.keys.remove((oldfreq, oldlast_oc, x))
            self.val_to_key[x] = (oldfreq + 1, self.i, x)
            self.key_to_val[(oldfreq + 1, self.i, x)] = x
            self.keys.add((oldfreq + 1, self.i, x))
        self.occurences[x].append(self.i)
        self.i += 1

    def pop(self) -> int:
        freq, _, x  = self.keys.pop() #self.key_to_val.popitem()[0]
        self.occurences[x].pop()
        if freq > 1: 
            # print(x, freq, self.occurences[x])
            self.key_to_val[(freq - 1, self.occurences[x][-1], x)] = x
            self.val_to_key[x] = (freq - 1, self.occurences[x][-1], x)
            self.keys.add((freq - 1, self.occurences[x][-1], x))
        else:
            del self.val_to_key[x]
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()



# Solution 3 defaultdict based solution


from collections import defaultdict
class FreqStack:

    def __init__(self):
        # dictionary -> key -> number, value -> no of occurrences
        self.frequency = defaultdict(int)
        
        # dictionary of stacks -> key -> frequency, value -> stack of numbers with said frequency
        self.stacks = defaultdict(list)
        
        # the current max frequency
        self.maxfrequency = 0

    def push(self, x: int) -> None:
        # number of occurrences of the value x
        self.frequency[x] += 1
        
        # check if 
        if self.frequency[x] in self.stacks:
            self.stacks[self.frequency[x]].append(x)
        else:
            self.stacks[self.frequency[x]] = [x]
        
        # update max frequency seen so far
        self.maxfrequency = max(self.maxfrequency, self.frequency[x])
        
        

    def pop(self) -> int:
        if self.maxfrequency == 0:
            return None
        
        else:
            latestmax = self.stacks[self.maxfrequency].pop(-1)
            # reduce the number of occurrences of the value
            self.frequency[latestmax] -= 1
            
            if len(self.stacks[self.maxfrequency]) == 0:
                self.maxfrequency -= 1
            
            return latestmax
    

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
