class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s = ''.join(ch for ch in s if ch.isalnum())
        b=s[::-1]

        if s==b:
            return True
        else:
            return False