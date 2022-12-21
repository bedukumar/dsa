class S:
    def splitString(self, s: str) -> bool:
        def dfs(index, prev):  # what comes: (1,4b),(2,3),(3,2),(4,1)
            if index == len(s):
                return True
            for j in range(index, len(s)):
                val = int(s[index:j+1])  # "3","2","1"
                # 3->2->1 so true<-true<-true
                if val + 1 == prev and dfs(j+1, val):
                    return True
            return False

        for i in range(len(s)-1):  # b
            val = int(s[:i+1])  # "4","43","432","4321"
            if dfs(i+1, val):
                return True
        return False


s = S()
x = s.splitString("0090089")
print(x)

# input="4321"

#                    "4321"
#                   .  ..   .
#                 /   /  \    \
#                4   43  432   4321
#               /|\    !    !     !
#              3,32,321
#             /   !  !
#            2
#           /
#          1

# because |32-4|!=1  and same goes for 43,432,4321 there descendant wont be just one less than their parents
