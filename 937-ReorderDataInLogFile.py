# Leetcode 937. Reorder Data in Log Files
# Easy 1/13/21


# You have an array of logs.  Each log is a space delimited string of words.

# For each log, the first word in each log is an alphanumeric identifier.  Then, either:

#     Each word after the identifier will consist only of lowercase letters, or;
#     Each word after the identifier will consist only of digits.

# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

# Return the final order of the logs.

 

# Example 1:

# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

 

# Constraints:

#     0 <= logs.length <= 100
#     3 <= logs[i].length <= 100
#     logs[i] is guaranteed to have an identifier, and a word after the identifier.


# Solution 1 pop numeric data and then sort alpha data.
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig_logs = []
        let_logs = []
        results = []
        i = 0
        
        while i < len(logs):
            key, data = logs[i].split(" ", maxsplit=1)
            if not data[0].isalpha():
                dig_logs.append(logs[i])
                logs.pop(i)
                
            else:
                i+=1
        for log in enumerate(logs):
            key,data = log[1].split(" ", maxsplit=1)
            let_logs.append([log[0], key, data])
            
        let_logs.sort(key=lambda x: x[1])
        let_logs.sort(key=lambda x: x[2])
        
        for log in let_logs:
            results.append(logs[log[0]])
        
        results += dig_logs
        return results


# T: O(ab)
# S: O(a)

# Solution 2 Hashmap

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if not logs:
            return []
        
        newlogwords = []
        newlognums = []
        
        mapp = collections.defaultdict(list)
        orderedmap = collections.defaultdict(list)
        
        
        for x in logs:
            temp = x.split()
            if temp[1].isnumeric():
                newlognums.append(x)
            else:
                mapp[temp[0]].append(temp[1:])
                
                newlogwords.append(temp[1:])
        
        newlogwords.sort()
        sortedkeys = sorted(mapp.keys())
        
        for x in sortedkeys:
            orderedmap[x] = mapp[x]
            
        for i,j in orderedmap.items():
            for x in j:
                if x in newlogwords:
                    index = newlogwords.index(x)
                    newlogwords[index] = str(i) + ' ' + ' '.join(newlogwords[index])
                    
        return newlogwords + newlognums

# T: O(a)
# S: O(a)