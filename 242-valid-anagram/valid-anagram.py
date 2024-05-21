class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if len(s) != len(t):
            return False
        else:
            if s:
                for letter in sorted(list(s)):
                    s_dict.update({letter: s_dict.get(letter, 0)+1})
            if t:
                for letter in sorted(list(t)):                    
                    t_dict.update({letter: t_dict.get(letter, 0)+1})
            return s_dict == t_dict