"""
    Trying to create my own trie structure here.
"""

class Node(object):
    def __init__(self):
        self.word = None
        self.nodes = {}

    def insert(self, word, position=0):
        # Check if word in self.
        char = word[position]
        if char not in self.nodes:
            # add to dictionary and create a new node.
            self.nodes[char] = Node()

        # Base case for the iteration.
        if position + 1 == len(word):
            self.nodes[char].word = word
            return True

        self.nodes[char].insert(word, position+1)

    def __get_all__(self):
        result = []

        # Iterate over and get all the words that are inside our trie.

        for key, value in self.nodes.items():
            result.extend(value.__get_all__())

        if self.word:
            result.append(self.word)
            return result

        return result

    def __get_words_by_prefix__(self, prefix, position):
        # Start looking until you find the prefix. and then iterate over its children and check for words.
        result = []
        if position < len(prefix):
            for key, val in self.nodes.items():
                current_letter = prefix[position]
                if key == current_letter:
                    print(key, val)
                    result += self.nodes[key].__get_words_by_prefix__(prefix, position + 1)
        else:
            for key, val in self.nodes.items():
                result += self.nodes[key].__get_words_by_prefix__(prefix, position + 1)
            if self.word:
                result.append(self.word)

        return result

    def __repr__(self):
        return str(self.word)


class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        self.root.insert(word, 0)

    def get_all(self):
        return self.root.__get_all__()

    def get_all_with_prefix(self, prefix):
        return self.root.__get_words_by_prefix__(prefix, 0)


if __name__ == '__main__':
    # Create the trie and insert some words then do some tests
    trie = Trie()
    trie.insert("go")
    trie.insert("gone")
    trie.insert("gi")
    trie.insert("cool") 
    trie.insert("comb")
    trie.insert("grasshopper")
    trie.insert("home")
    trie.insert("hope")
    trie.insert("hose")

    print(trie.get_all_with_prefix("gra"))
    # print("\n")