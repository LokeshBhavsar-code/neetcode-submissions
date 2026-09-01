class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      
            if len(s) != len(t):
                return False

            alp = [0] * 26

            for i in range(len(s)):
                alp[ord(s[i]) - ord('a')] += 1
                alp[ord(t[i]) - ord('a')] -= 1

            return all(x == 0 for x in alp)