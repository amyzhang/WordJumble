class dictTrie:
    def __init__(self, dictname):
        #read dictionary in from dictname
        with open(dictname) as f:
            content = [line.rstrip() for line in f]
        self.root = [[], {}]
        for word in content:
            self.insert(word)

    def insert(self, word):
        curr_node = self.root
        sortedw = ''.join(sorted(word))
        for ch in sortedw:
            curr_node = curr_node[1].setdefault(ch, [[], {}])
        curr_node[0].append(word)
        
    def find(self, word):
        sortedw = ''.join(sorted(word))
        jumble = set()
        self.find_helper(self.root, sortedw, jumble)
        return jumble
    
    def find_helper(self, node, word, jumble):
        if len(word)>1:
            self.find_helper(node, word[1:], jumble)
        try:               
            curr_node = node[1][word[0]]
            jumble.update(curr_node[0])
        except KeyError:
            return
        if len(word)>1:
            self.find_helper(curr_node, word[1:], jumble)
        
if __name__ == "__main__":
    d = dictTrie('dicts/2of4brif.txt')
    while True:
        seed = raw_input("Enter a string: ")
        print d.find(seed)
    
