class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        c = []

        for i in range(len(mat)):
            c.append([i, self.count_ones(mat[i])])

        weakest = []

        for e in sorted(c, key=lambda r:r[1]):
            weakest.append(e[0])
        return weakest[:k]

    def count_ones(self, a):
        count = 0

        for i in range(len(a)):

            if a[i] == 1:
                count += 1

        return count