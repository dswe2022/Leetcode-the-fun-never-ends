
# Leetcode 125. Valid Palindrome
# Easy 12/25/20

# Solution 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s) 
        if s == s[::-1]: 
            return True
        else:
            return False

# T: O(a)
# S: O(a)



# Solution 2

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = -1
        j = len(s)
        while True:
            i += 1
            j -= 1
            if i > j:
                return True
            while i < j:
                if not s[i].isalnum():
                    i += 1
                else:
                    break
            while i < j:
                if not s[j].isalnum():
                    j -= 1
                else:
                    break
            if s[i].lower() != s[j].lower():
                return False


# T: O(a)
# S: O(a)


# Solution 3


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanlist = [c for c in s.lower() if c.isalnum()]
        return cleanlist == cleanlist[::-1]

# T: O(a)
# S: O(a)

