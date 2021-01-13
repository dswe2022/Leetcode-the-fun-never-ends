# Leetcode 127. Word Ladder

# Given two words beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

#     Only one letter can be changed at a time.
#     Each transformed word must exist in the word list.

# Return 0 if there is no such transformation sequence.

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.

# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

 

# Constraints:

#     1 <= beginWord.length <= 100
#     endWord.length == beginWord.length
#     1 <= wordList.length <= 5000
#     wordList[i].length == beginWord.length
#     beginWord, endWord, and wordList[i] consist of lowercase English letters.
#     beginWord != endWord
#     All the strings in wordList are unique.



class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        count = 0
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        queue = [beginWord]

        while(len(queue) > 0):
            
            size = len(queue)
            count += 1

            for _i in range(size):
                node  = queue.pop(0)
            
                if node == endWord:
                    return count

                neighbors = self.get_neighbors(node, word_set)
                for neighbor in neighbors:
                    queue.append(neighbor)

        return 0

    # using 26 letters is better than check every nodes in wordList
    # l = length of word
    # 26 letters = O(l * 25 * l)
    # each word has l * 25 variation, and to check or change each attempt using l
    #
    # check every nodes in wordlist = O(l * N * N)
    # to check neighbors of every word in the list needs l * N, and there are N such words
    def get_neighbors(self, word, word_set):
        results = []
        for i in range(len(word)):
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                if letter == word[i]:
                    continue

                neighbor = word[:i] + letter + word[(i + 1):]
                if neighbor not in word_set:
                    continue
                    
                results.append(neighbor)
                word_set.remove(neighbor) #this is important

        return results

# T: O(l * N * N)
# S: O(a)