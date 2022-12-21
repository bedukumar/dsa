from typing import List


class Solution:
    def permutation(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permutation(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result


s = Solution()
l = s.permutation([1, 2, 3])
print(l)

# >> > type(l[:])
# <class 'list' >
