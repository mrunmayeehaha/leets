class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'
        s += '+'

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == ' ':
                continue
            else:
                if sign == '+':
                    stack.append(num)
                    
                elif sign == '-':
                    stack.append(-num)

                elif sign == '*':
                    stack[-1] *= num

                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)

                sign = ch
                num = 0

        return sum(stack)