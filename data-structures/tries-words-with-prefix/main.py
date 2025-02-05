class Trie:
    def search_level(self, cur, cur_prefix, words):
        if self.end_symbol in cur:
            words.append(cur_prefix)
        for key in sorted(cur.keys()):
            if key != self.end_symbol:
                self.search_level(cur[key], cur_prefix + key, words)
        return words

    def words_with_prefix(self, prefix):
        matches = []
        current = self.root
        for char in prefix:
            if char not in current:
                return []  # Prefix not found, return an empty list
            current = current[char]
        return self.search_level(current, prefix, matches)


    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True
