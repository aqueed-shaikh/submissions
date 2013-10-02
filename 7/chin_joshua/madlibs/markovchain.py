import re
import random

class MarkovChain:

    def __init__(self, source, length=4):
        chain = {}
        words = re.split("\s+", source)
        for index, word in enumerate(words):
            if index < length:
                continue
            link = tuple(words[index-length:index])
            end = tuple(words[index-length+1:index+1])
            if link in chain:
                chain[link].append(end)
            else:
                chain[link]=[end]
        self.chain = chain
        self.length = length

    def __iter__(self):
        self._generate(None)

    def generate(self, length):
        return " ".join(self._generate(length))

    def _generate(self, length):
        link = random.choice(list(self.chain.keys()))
        for i in link:
            yield i
        count = 0
        while link in self.chain:
            link=random.choice(self.chain[link])
            yield link[-1]
            if length is not None:
                count += 1
                if count >= length: break

    def branch_factor(self):
        out = 0
        for key, item in self.chain.items():
            out += len(item)
        return out/len(self.chain)

    def __len__(self):
        return len(self.chain)

    def __repr__(self):
        return repr(self.chain)
    
if __name__=='__main__':
    print(MarkovChain("".join(open("Alice.txt")), length=3).generate(100))
    
