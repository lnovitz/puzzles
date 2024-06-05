class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
        return res 
        # so we need to keep track if characters are unique - dictionary of each character.
        # if it increments > 1 for any character, 
        # then splice the current substring up to the index of the dupe character
        # and then loop through 
        # abcabcbb
        # a, b, c, 
        # len(3)
        # a b c 
        # len(3)
        # b b 
        # len(2)

        #abcade
        # a, b, c
        # len(3)
        # a, d, e
        # len(3)
        # b, c, a, d, e
        # len(5) 
        # n * (n - 1)

        