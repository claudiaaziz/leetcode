class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True
    






class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes
        self.children = {}
        # Flag to indicate if this node represents the end of a word
        self.end_of_word = False

class Trie:
    def __init__(self):
        # Initialize the Trie with an empty root node
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root

        # Traverse the Trie, creating nodes as needed
        for char in word:
            #Make a TreeNode for char if it doesn't exist
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        # Mark the end of the inserted word
        curr.end_of_word = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        
        # Traverse the Trie to search for the word
        for char in word:
            #Can return False if char is not in children
            if char not in curr.children:
                return False
            curr = curr.children[char]

        # Check if the last node represents the end of a word
        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        # Traverse the Trie to check if the prefix exists
        for char in prefix:
            #Can return False if char is not in children
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        #Went through the whole thing without returning False, so the prefix exists
        return True
