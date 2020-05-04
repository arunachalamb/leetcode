# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
N = 2126753390
F = 1702766719

def isBadVersion(version):
    if version >= F:
        return True
    else:
        return False

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
                return 1
        i0 = 1
        i1 = n
        while i1 > i0:
            i0v = isBadVersion(i0)
            i1v = isBadVersion(i1)
            if i0v == False and i1v == True:
                print('FT', i0, i1)
                if i1 - i0 == 1:
                    return i1
                else:
                    i1 -= (i1 - i0)//2
                print(i0, i1)
            elif i0v == False and i1v == False:
                print('FF', i0, i1)
                _i0 = i0
                i0 = i1
                i1 += (i1 - _i0)*2
                if i1 > n:
                    i1 = n
                print(i0, i1)
            elif i0v == True and i1v == True:
                print('TT', i0, i1)
                _i0 = i0
                i1 = i0
                i0 = _i0//2
                if i0 < 1:
                    i0 = 1
                print(i0, i1)
        return i1

if __name__ == '__main__':
    print(Solution().firstBadVersion(N))
