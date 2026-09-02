class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'{':'}', '[':']', '(':')'}
        for c in s:
            if c in brackets.keys():
                stack.append(c)
            elif stack and c == brackets.get(stack[-1],""):
                stack.pop()
            else:
                return False
        
        return True if len(stack) == 0 else False