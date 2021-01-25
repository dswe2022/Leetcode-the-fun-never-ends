# Leetcode 126. Word Ladder II
# Hard 1/25/21 

# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: []

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

# Solution 1

# SolutionWithBFS:
class Solution():
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        """
        To let successful exploration by level, we need visited and visitedAtThisLevel sets.
        Append newly found words to visitedAtThisLevel, and not in visited since for other
        paths in exploration "nextWord" could be the critical word required
        to form the shortest path
                       hit
                     /     \
                  hot      lit
                /     \    /  \
              dot      lot     lig
                 \   /     \  /
                  dog      log
                      \   /
                       cog
        For example in this diagram, if previous items in queue were
        [hit, hot] and [hit, lit], then in the next level iteration if we mark
        "lot" as visited when coming from [hit, hot], then "lot" will
        no longer be visible to [hit, lit]. So it is important that we let
        other nodes at the same level still "explore" a visited node. After
        the level exploration is finished th¨en we can mark the nodes
        dot, lot and lor together as visited.
        """

        if not endWord or endWord not in wordList:
            return []

        # build genericWord to actual words map
        wordMap = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                genericWord = word[:i] + "*" + word[i + 1 :]
                wordMap[genericWord].append(word)

        q = deque()
        q.append([beginWord])
        found = False
        visited = {beginWord}
        output = []
        while q and not found:
            itemsAtThisLevel = len(q)
            visitedAtThisLevel = set()
            for _ in range(itemsAtThisLevel):
                currentPath = q.popleft()
                lastWord = currentPath[-1]
                for i in range(len(lastWord)):
                    genericWord = lastWord[:i] + "*" + lastWord[i + 1 :]
                    for nextWord in wordMap[genericWord]:
                        if nextWord == endWord:
                            output.append(currentPath + [endWord])
                            found = True
                        if nextWord not in visited:
                            q.append(currentPath + [nextWord])
                            visitedAtThisLevel.add(nextWord)
            visited = visited.union(visitedAtThisLevel)

        return output


# Solution 2
# SolutionWithBFSandDFS:
class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        """
        Run a BFS to determine the smallest distance to reach endWord and
        at the same time to build the adjacency list of every traversed node's
        parent to child relationship that follows the property of:
        -- The child should strictly be one level below to the parent
        -- The child should be a part of the valid transformation of the parent

        For the following graph:
                       hit
                     /     \
                  hot      lit
                /     \    /  \
              dot      lot     lig
                 \   /     \  /
                  dog      log
                      \   /
                       cog

        The adjacency list "children" will be of kind:
        {
            "hit": {hot, lit}
            "hot": {dot, lot},
            "lit": {lot, lig},
            "dot": {dog},
            "lot": {log, dog},
            "lig": {log},
            "dog": {cog},
            "log": {cog}
        }

        When we have the two things 1) shortest distance 2) children adj list
        then we can "blindly" run a backtracking with DFS that terminates when:
        -- The depth is equal to shortest distance

        The backtracking will append to the output when
        -- The node and the end of the shortest distance is the endWord
        """
        if not endWord or endWord not in wordList:
            return []

        # build genericWord to actual words map
        wordMap = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                genericWord = word[:i] + "*" + word[i + 1 :]
                wordMap[genericWord].append(word)

        q = deque()
        q.append(beginWord)
        found = False
        visited = {beginWord}
        children = defaultdict(set)
        depth = 0

        # Run BFS and find the shortest route to the endWord. Also
        # build a special adjacency list "children" that maps the child
        # nodes of every node from beginWord to endWord
        while q and not found:
            depth += 1
            itemsAtThisLevel = len(q)
            visitedAtThisLevel = set()
            for _ in range(itemsAtThisLevel):
                word = q.popleft()
                for i in range(len(word)):
                    genericWord = word[:i] + "*" + word[i + 1 :]
                    for nextWord in wordMap[genericWord]:
                        if nextWord == word:
                            continue  # same level
                        if nextWord not in visited:
                            if nextWord == endWord:
                                found = True
                            # This is the most important step
                            children[word].add(nextWord)
                            q.append(nextWord)
                            visitedAtThisLevel.add(nextWord)
            visited = visited.union(visitedAtThisLevel)

        output = []

        def dfs(currentWord, currentPath, currentDistance):
            if currentDistance > depth:
                return
            if currentDistance == depth and currentWord == endWord:
                output.append(currentPath)
                return
            for child in children[currentWord]:
                dfs(child, currentPath + [child], currentDistance + 1)

        dfs(beginWord, [beginWord], 0)
        return output