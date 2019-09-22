#!/usr/bin/env python


class Trie:
    """
    Simple trie data structure implementation.
    """
    class Node:
        """
        Simple trie node implementation.
        """
        def __init__(self, char):
            """Initialize node.
            """
            self.char = char  # Node label
            self.children = []
            self.eow = False  # End of word node.

        def get(self, char):
            """Find child node.

            :char: Label of desired child.
            :returns: Child node if found, `None` otherwise.

            """
            index = None
            for child in self.children:
                if child.char == char:
                    index = self.children.index(child)
                    break
            if index is not None:
                return self.children[index]

        def add(self, char):
            """Add new child node.

            :char: Label of child to be added.

            """
            new_node = Trie.Node(char)
            self.children.append(new_node)
            self.children.sort()
            return new_node

        def empty(self):
            """Check if node has children.

            :returns: True if node has children, False otherwise.

            """
            return self.children == []

        def remove(self, char):
            """Remove child node.

            :char: Label of child node to be removed.

            """
            found_child = None
            for child in self.children:
                if child.char == char:
                    found_child = child
                    break
            if found_child is not None:
                self.children.remove(found_child)

        def __lt__(self, other):
            return self.char.__lt__(other.char)

        def __gt__(self, other):
            return self.char.__gt__(other.char)

        def __le__(self, other):
            return self.char.__le__(other.char)

        def __ge__(self, other):
            return self.char.__ge__(other.char)

        def __eq__(self, other):
            return self.char.__eq__(other.char)

        def __ne__(self, other):
            return self.char.__ne__(other.char)

    def __init__(self, words=None):
        """Initialize the trie.

        :words: List of words to be inserted into trie.

        """
        self.root = Trie.Node('*')
        if words is not None:
            for word in words:
                self.add(word)

    def add(self, word):
        """Insert a word into the trie.

        :word: Key to insert into trie.

        """
        node = self.root
        for char in word:
            found_in_child = False
            for child in node.children:
                if child.char == char:
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                node = node.add(char)
        node.eow = True

    def add_many(self, words):
        """Insert multiple words into the trie.

        :words: List of keys to insert into trie.

        """
        for word in words:
            self.add(word)

    def contains(self, word):
        """Check if trie contains word.

        :word: Word to check membership.
        :returns: True if trie contains word, and False otherwise.

        """
        def _contains(node, word):
            if len(word) == 1:
                child = node.get(word)
                if (
                    child is not None and
                    word == child.char and
                    child.eow
                ):
                    return True
                else:
                    return False
            else:
                char = word[0]
                word = word[1:]
                child = node.get(char)
                if child is None:
                    return False
                else:
                    return _contains(child, word)

        return False if self.empty() else _contains(self.root, word)

    def empty(self):
        """Check if trie is empty.

        :returns: True if trie is empty, False otherwise.

        """
        return self.root.empty()

    def list_words(self):
        """Get all words in trie.

        :returns: A list containing all words obtainable from traversing
                  the trie.

        """
        words = []

        def _list_words(words, node, prefix=''):
            new_prefix = prefix + node.char
            if node.eow:
                words.append(new_prefix)
            for child in node.children:
                _list_words(words, child, new_prefix)

        for child in self.root.children:
            _list_words(words, child)

        return words

    def prefixes_of(self, word):
        """Get all prefixes of word in trie.

        :returns: A list containing all words in trie that are prefixes to
                  word.

        """
        prefixes = []
        initial_node = self.root.get(word[0])
        prefix = ''

        def _prefixes_of(node, prefixes, prefix, word):
            if word != '':
                word = word[1:]
                prefix += node.char
                if node.eow:
                    prefixes.append(prefix)
                if word != '':
                    next_node = node.get(word[0])
                    _prefixes_of(next_node, prefixes, prefix, word)

        _prefixes_of(initial_node, prefixes, prefix, word)

        if prefixes != []:
            prefixes = prefixes[:-1]

        return prefixes

    def remove(self, word):
        """Remove a word from the trie.

        :word: Key to remove from trie.

        """
        def _remove(root, key, depth=0):
            if depth == len(key):
                if root.eow:
                    root.eow = False

                if root.empty():
                    root = None
                return root

            char = key[depth]
            child = root.get(char)
            result = _remove(child, key, depth + 1)

            if result is None:
                root.remove(char)

            if root.empty() and root.eow is False:
                root = None

            return root

        return None if not self.contains(word) else _remove(self.root, word)

    def remove_many(self, words):
        """Remove multiple words from the trie.

        :words: List of keys to remove from trie.

        """
        for word in words:
            self.remove(word)

    def save(self, filename='words.txt'):
        """Save words in trie to file.

        :filename: File to which the words are saved to,
                   file is created if. it does not exist.
        """
        try:
            with open(filename, 'w') as file:
                words = self.list_words()
                for word in words:
                    file.write(word + '\n')
        except:
            print(f'something went wrong when trying to write to {filename}.')

    def load(self, filename='words.txt'):
        """Load words found in file into trie.

        :filename: File from which to read from.
        """
        self.root = Trie.Node('*')
        try:
            with open(filename) as file:
                words = file.read().split()
                for word in words:
                    self.add(word)
        except:
            print(f'{filename} is not a valid file, loading empty Trie.')
