class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')':'(', '}': '{', ']': '['}
        stack = []
        if len(s) == 1:
            return False
        
        for char in s:
            if char not in closeToOpen:
                stack.append(char)
            else:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False

            