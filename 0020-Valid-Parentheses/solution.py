class Solution(object):
    def isValid(self, s):
        stack=[]
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack:
                    return False
                elif i ==")" and stack[-1]=='(':
                    stack.pop(-1)
                elif i =="}" and stack[-1]=='{':
                    stack.pop(-1)
                elif i =="]" and stack[-1]=='[':
                    stack.pop(-1)
                else:
                    return False
        return len(stack) == 0