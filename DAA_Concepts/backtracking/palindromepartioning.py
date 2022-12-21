class Solution:
    def partioning(self, l):
        res = []
        part = []

        def get_partition(i):
            if i == len(l):
                res.append(part[:])
                return
            for j in range(i, len(l)):
                if isPal(l, i, j):
                    part.append(l[i:j+1])
                    get_partition(j+1)
                    part.pop()

        def isPal(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i+1, j-1
            return True

        get_partition(0)
        return res


s = Solution()
x = s.partioning("aab")
print(x)
