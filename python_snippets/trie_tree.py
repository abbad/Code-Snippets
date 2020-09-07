# I wonder if make this a child of a dictionary is more elegant.
class Node:
    
    def __init__(self, key, children=None):
        
        self.key = key
        # I had this as a list, but changed it to dictionary.
        # having it as a set made it hard to hash.
        self.children = children or {}
        self.is_word = False
        
    def __eq__(self, other):
        return other == self.key
    
    def __repr__(self):
        return str(self.key)


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.start = Node('*')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.start
        current_keys = self.start.children
        
        for char in word: 
            if char not in current_keys:
                node = Node(char)
                current_keys[char] = node
                current_keys = node.children
                node = node
            else:
                node = current_keys[char]
                current_keys = node.children

        node.is_word = True

    def search(self, word: str, start_node=None) -> bool:
        """
        Returns if the word is in the trie, also supports wild card .
        """
        node = start_node or self.start
        children = node.children
        
        for index, char in enumerate(word): 
            # this is how I implemented it,
            # if there was a dot, skip this iteration
            # and go after all the children of the current child.
            if char == '.':
                for key, child in children.items():
                    if word[index+1:] == '':
                        return True

                    if self.search(word[index+1:], child):
                        return True
            elif char in children:
                node = children[char]
                children = node.children
            else:
                return False

        if node.is_word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        children = self.start.children
        node = self.start
        for char in prefix: 
          
            if char in children:
                node = children[char]
                children = node.children
            else:
                return False

        return True


def traverse_trie(trie):
    if not trie:
        return

    where_are_we = [trie]
  
    while(where_are_we):

        val = where_are_we.pop()

        for item, node in val.children.items():
            print('key ' + str(item) + ' is_word ' + str(node.is_word) , end=' ')
            where_are_we.append(node)

    print()


t = Trie()

t.insert('abc')
t.insert('allen')
traverse_trie(t.start)

# t.insert('tony')

print(t.search('a'))

print(t.startsWith('allenx'))


