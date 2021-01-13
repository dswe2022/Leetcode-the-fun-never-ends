# Leetcode 208. Implement Trie (Prefix Tree)
# Medium 12/29/20 


# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true


# Solution 1
class TrieNode:

    def __init__(self):
        self.children = [0]*26
        self.end = False

    def put(self, ch):
        self.children[ord(ch)-ord('a')] = TrieNode()

    def get(self, ch):
        return self.children[ord(ch)-ord('a')]

    def contains_key(self, ch):
        return self.children[ord(ch)-ord('a')] != 0

    def set_end(self):
        self.end = True

    def is_end(self):
        return self.end


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for i in range(len(word)):
            if not curr.contains_key(word[i]):
                curr.put(word[i])
            curr = curr.get(word[i])

        curr.set_end()


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for i in range(len(word)):
            if not curr.contains_key(word[i]):
                return False
            curr = curr.get(word[i])

        return True if curr.is_end() else False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for i in range(len(prefix)):
            if not curr.contains_key(prefix[i]):
                return False
            curr = curr.get(prefix[i])

        return True


# T: O(a)
# S: O(a)