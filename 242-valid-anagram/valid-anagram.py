class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            # now we need to count each letter
            scounter = dict()
            for letter in s:
                if letter in scounter.keys():
                    scounter[letter] += 1
                else:
                    scounter[letter] = 1
            tcounter = dict()
            for letter in t:
                if letter in tcounter.keys():
                    tcounter[letter] += 1
                else:
                    tcounter[letter] = 1
            if scounter == tcounter:
                return True
            else:
                return False


test = Solution()
s1 = "anagram"
t1 = "nagaram"
s2 = "rat"
t2 = "car"
assert test.isAnagram(s=s1, t=t1) == True
assert test.isAnagram(s=s2, t=t2) == False
