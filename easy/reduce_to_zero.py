class Solution:
    def numberOfSteps(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        if n % 2 == 0:
            return 1 + self.numberOfSteps(n//2)

        return 1 + self.numberOfSteps(n-1)

    # Solution 2 - Bit manipulation
    def numberOfSteps(self, n: int) -> int:
        if n == 0:
            return 0

        steps = 0

        while n != 1:
            steps += (1 + (n & 1))
            n = n >> 1

        return steps+1
