class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        map={")":"(","]":"[","}":"{"}
        for c in s:
            if c in map:
                if stack and stack[-1]==map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack