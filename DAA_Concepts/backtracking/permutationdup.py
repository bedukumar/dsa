from typing import List


class PermutationsDup:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []

        count = {n: 0 for n in nums}
        for n in nums:
            count[n] += 1

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    dfs()
                    count[n] += 1
                    perm.pop()
        dfs()
        return res


p = PermutationsDup()
print(p.permuteUnique([1, 1, 2]))


# x = [1, 1, 2, 1, 3, 3]

# count = {n: 0 for n in x}
# count.update({4: 0})
# print(count)
# # for n in x:
# #     count[n] += 1

# for n in count:
#     print(n, count[n])
