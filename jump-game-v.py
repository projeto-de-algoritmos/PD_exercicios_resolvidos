class Solution:
    def maxJumps(self, arr, d) -> int:
        n = len(arr)
        dp = [0] * n

        def calc(i, d):
            if dp[i] > 0:
                return dp[i]

            j = i - 1
            jump = 1

            while j >= max(0, i - d) and arr[j] < arr[i]:
                jump = max(jump, calc(j, d) + 1)
                j -= 1

            j = i + 1

            while j <= min(n - 1, i + d) and arr[j] < arr[i]:
                jump = max(jump, calc(j, d) + 1)
                j += 1

            dp[i] = jump
            return jump

        result = 1
        for i in range(n):
            result = max(result, calc(i, d))
        return result
