class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        n = 0
        i = 0

        while i < len(s):
            c = romans[s[i]]

            if i+1 != len(s):
                t = romans[s[i+1]]

                if c >= t:
                    n += c
                else:
                    n += (t - c)
                    i += 1
            else:
                n += c

            i += 1

        return n
