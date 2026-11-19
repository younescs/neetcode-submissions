class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []

        for tok in tokens:
            if tok == "+":
                ans.append(ans.pop() + ans.pop())
            elif tok == "*":
                ans.append(ans.pop() * ans.pop())
            elif tok == "/":
                num2, num1 = ans.pop(), ans.pop()
                ans.append(int(num1/num2))
            elif tok == "-":
                num2, num1 = ans.pop(), ans.pop()
                ans.append(num1 - num2)
            else:
                ans.append(int(tok))

        return ans[0]
        