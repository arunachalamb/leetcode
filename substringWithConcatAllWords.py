# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

from itertools import permutations

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not len(s) or not len(words): return []
        a = [''.join(i) for i in list(permutations(words, len(words)))]
        print(a)
        r = []
        for w in a:
            for m in re.finditer(w[0], s):
                if s[m.start():m.start()+len(w)] == w:
                    r.append(m.start())
        return list(set(r))
