class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted_s = [x.lower() for x in s if x.isalnum()]
        for i in range(0, len(converted_s), 1):
            j = len(converted_s) - 1 - i
            if converted_s[i] == converted_s[j]:
                continue
            else:
                return False
        return True
                