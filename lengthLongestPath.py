class Solution:
    def lengthLongestPath(self, input: str) -> int:
        import re
        s = re.split('\n',input)
        d = s[0]
        print(input,len(input))
        print('d',d)
        if len(s) == 1 and '.' in input:
            print('ret 1 file')
            return len(input)
        s = s[1:]
        m = 0
        l = 0
        pl = 0
        cl = {}
        cl[0] = len(d)
        for i in range(len(s)):
            print(s[i])
            k = len(re.findall('\t',s[i]))
            if k == 0:
                v = len(s[i].replace('\t',''))
            else:
                v = len(s[i].replace('\t','')) + 1
            cl[k] = v
            if '.' in s[i]:
                if k < pl:
                    for _k in range(k+1,max(cl)+1):
                        del cl[_k]
                for _k in cl:
                    l = l + cl[_k]
                if m < l:
                    m = l
                l = 0
                print('dot',m,cl,k,v,pl)
            else:
                if k < pl:
                    for _k in range(k+1,max(cl)+1):
                        del cl[_k]
                print('else',m,cl,k,v,pl)
            pl = k
        return m

if __name__ == '__main__':
    Sol = Solution()
    """
    r = Sol.lengthLongestPath('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext')
    print(r)
    r = Sol.lengthLongestPath('file1.txt\nfile2.txt\nlongfile.txt')
    print(r)
    r = Sol.lengthLongestPath('a')
    print(r)
    r = Sol.lengthLongestPath('a.txt')
    print(r)
    r = Sol.lengthLongestPath('a\n\taa\n\t\taaa\n\t\t\tfile1.txt\naaaaaaaaaaaaaaaaaaaaa\n\tsth.png')
    print(r)
    """
    r = Sol.lengthLongestPath('a\n\tb\n\t\tc.txt\n\taaaa.txt')
    print(r)
