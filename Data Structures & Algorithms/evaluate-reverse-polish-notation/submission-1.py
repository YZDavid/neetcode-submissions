class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                res = str(int(eval(a + token + b)))
                stack.append(res)
            else:
                stack.append(token)

        return int(stack.pop())

