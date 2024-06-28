class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = collections.deque([1])
        for each in nums:
            prefix.append(prefix[-1] * each)

        suffix = collections.deque([1])
        for each in nums[::-1]:
            suffix.appendleft(suffix[0] * each)

        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[i + 1])

        return ans

