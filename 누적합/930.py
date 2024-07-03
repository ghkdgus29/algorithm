class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = collections.Counter()

        s = [0]
        for num in nums:
            s.append(s[-1] + num)

        ans = 0
        for val in s:
            if val - goal in counter:
                ans += counter[val - goal]
            counter[val] += 1
        return ans
