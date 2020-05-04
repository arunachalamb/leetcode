from collections import Counter

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        _S = Counter(S)
        _sum = 0
        for e in set(_S).intersection(set(J)):
            _sum += _S[e]
        return _sum
