class Solution:
    def pivotInteger(self, n: int) -> int:
        s = [0]
        for val in range(1, n + 1):
            s.append(s[-1] + val)

        for i in range(1, n + 1):
            if s[i] == s[-1] - s[i - 1]:
                return i

        return -1
