class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn_freq = self.freq_map(ransomNote)
        m_freq = self.freq_map(magazine)

        for c in ransomNote:
            if c not in m_freq or m_freq[c] < rn_freq[c]:
                return False

        return True

    def freq_map(self, s):
        freq = {}

        for i in range(len(s)):

            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 0

        return freq
