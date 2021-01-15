# Leetcode 642. Design Search Autocomplete System
# Hard 1/14/21

# Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

#     The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
#     The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
#     If less than 3 hot sentences exist, then just return as many as you can.
#     When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.

# Your job is to implement the following functions:

# The constructor function:

# AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.

# Now, the user wants to input a new sentence. The following function will provide the next character the user types:

# List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.
 

# Example:
# Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
# The system have already tracked down the following sentences and their corresponding times:
# "i love you" : 5 times
# "island" : 3 times
# "ironman" : 2 times
# "i love leetcode" : 2 times
# Now, the user begins another search:

# Operation: input('i')
# Output: ["i love you", "island","i love leetcode"]
# Explanation:
# There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

# Operation: input(' ')
# Output: ["i love you","i love leetcode"]
# Explanation:
# There are only two sentences that have prefix "i ".

# Operation: input('a')
# Output: []
# Explanation:
# There are no sentences that have prefix "i a".

# Operation: input('#')
# Output: []
# Explanation:
# The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.
 

# Note:

#     The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
#     The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
#     Please use double-quote instead of single-quote when you write test cases even for a character input.
#     Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.

# Solution 1 Using Trie Tree Easier solution



class TrieNode:
    def __init__(self):
        self.children = {}
        self.freq = {}

class AutocompleteSystem:

    # Included
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        
        for i, sen in enumerate(sentences):
            self.add(sen, times[i])
        
        self.node = self.root
        self.cur = ""

    # Included
    def input(self, c: str) -> List[str]:
        if c == "#":
            self.add(self.cur, 1)
            self.node = self.root
            self.cur = ""

        if c != "#":
            self.cur += c
        
            if c in self.node.children:
                self.node = self.node.children[c]
                res_dict = self.node.freq
                res = sorted(res_dict.items(), key = lambda item: (-item[1], item[0]))[:3] 
                ans = []
                for item in res:
                    ans.append(item[0])

                if len(ans) == 0:
                    self.add_new(c)

                return ans
            else:
                self.node = TrieNode()
                
    def add(self, sen, freq):
        node = self.root
        for s in sen:
            if s not in node.children:
                node.children[s] = TrieNode()
            node = node.children[s]
            if sen in node.freq:
                node.freq[sen] += freq
            else:
                node.freq[sen] = freq




# Solution 2
# TLDR: Create a trie, each trie node stores all sentences that pass through it (don't have to traverse each subtree each time), 
# then add some sort logic on top to ensure we return the autocompletes in the correct order which is specified.

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}
        self.subs = set()
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def setup(self, words):
        for word in words:
            self.add(word)
            
    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node.subs.add(word)
            node = node.children[c]
        node.subs.add(word)
        node.word = True
        
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return ''
            else:
                node = node.children[c]
        return node.subs
                

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.sentences = sentences
        self.times = times
        self.cnts = collections.defaultdict(int)
        self.ords = collections.defaultdict(list)
        self.trie = Trie()
        self.trie.setup(sentences)
        self.ins = ''
        self.add_cnts()
        
    def add_cnts(self):
        for i in range(len(self.times)):
            self.cnts[self.sentences[i]] = self.times[i]
            self.sorter(self.sentences[i]) 
        
    def sorter(self, sent):
        if sent not in self.ords:
            self.ords[sent] = [ord(c) for c in sent]

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.trie.add(self.ins)
            self.cnts[self.ins] += 1
            self.sorter(self.ins)
            self.ins = ""
            return []
        self.ins += c
        sents = list(self.trie.search(self.ins))
        sents.sort(key=lambda x: self.ords[x])
        sents.sort(key=lambda x: -self.cnts[x])
        return sents[:3]




# Solution 3 Using Trie Tree

class TrieNode:
    def __init__(self, val='.'):
        self.val = val
        self.neibs = dict()
        self.sentence_indices = set()
    
    def get_top_3_sentences(self, trie, acs):
        
        candidates = []
        for sent in self.sentence_indices:
            sentence = trie.sentences[sent]
            freq = acs.sentence_map[sentence][1]
            candidates.append([sentence, freq]) 
            
        if candidates:
            candidates.sort(key = lambda x: (-x[1], x[0]))
        
        return [i for i,j in candidates[:3]]
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.sentences = []

    def insert(self, sent_index):
        self.insert_by_char(self.root, sent_index, 0)

    def insert_by_char(self, node, sent_index, word_index):
        sentence = self.sentences[sent_index]
        ch = sentence[word_index]

        if ch not in node.neibs:
            node.neibs[ch] = TrieNode(ch)

        next_node = node.neibs[ch]
        next_node.sentence_indices.add(sent_index)

        if word_index==len(sentence)-1:
            return

        self.insert_by_char(node.neibs[ch], sent_index, word_index+1)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        from collections import defaultdict
        self.sentence_map = defaultdict(list)

        self.trie = Trie()
        self.trie.sentences = sentences

        for sent_index, freq in enumerate(times):
            sentence = self.trie.sentences[sent_index]
            self.sentence_map[sentence] = [sent_index, freq]
            self.trie.insert(sent_index)

        self.prev = []
        self.curr = self.trie.root

    def input(self, c: str) -> List[str]:
        if c == '#':
            new_sentence = "".join(self.prev)
            if  new_sentence not in self.sentence_map:
                self.trie.sentences.append(new_sentence)
                self.sentence_map[new_sentence]= [len(self.trie.sentences)-1, 1]
            else:
                self.sentence_map[new_sentence][1]+=1

            self.trie.insert(self.sentence_map[new_sentence][0])
            self.prev = []
            self.curr = self.trie.root
            return []
            
        else:
            self.prev.append(c)
            if c not in self.curr.neibs:
                new_node = TrieNode(c)
                self.curr.neibs[c]=new_node
            self.curr = self.curr.neibs[c]
            return self.curr.get_top_3_sentences(self.trie, self)

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
