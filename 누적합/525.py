class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        s = [0]
        for val in nums:
            if val == 0:
                s.append(s[-1] - 1)
            else:
                s.append(s[-1] + 1)

        start = {0: 0}
        end = {}
        for idx, val in enumerate(s):
            if val not in start:
                start[val] = idx
            else:
                end[val] = idx

        ans = 0
        for val in end.keys():
            ans = max(ans, end[val] - start[val])
        return ans
