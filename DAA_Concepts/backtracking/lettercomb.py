class S:
    def letterComb(self, digits):
        res = []
        digitstoChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def Backtrack(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                print(currStr)
                return
            print(currStr)
            for x in digitstoChar[digits[i]]:
                Backtrack(i+1, currStr+x)
                print(currStr)

        if digits:
            Backtrack(0, "")
        return res


s = S()
x = s.letterComb("23")
print(x)
