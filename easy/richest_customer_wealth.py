class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for acc in accounts:
            wealth = self.array_sum(acc)

            if wealth > max_wealth:
                max_wealth = wealth

        return max_wealth

    def array_sum(self, arr):
        return sum(arr)
