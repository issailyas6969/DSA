class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        for token in tokens:
            if token in {"+","-","*","/"}:
                a=stack.pop()
                b=stack.pop()
                if token=="+":
                    r=a+b
                elif token=="-":
                    r=b-a
                elif token=="*":
                    r=a*b
                elif token=="/":
                    r=int(float(b)/a)
                stack.append(r)
            else:
                stack.append(int(token))
        return stack[-1]


        