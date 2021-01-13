# Leetcode 150 Evaluate Reverse Polish Notation
# Medium 12/17/20 

# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.


class Solution:
    def evalRPN(self, arr: List[str]) -> int:
        arr = arr[::-1]
        stk = []

        while arr:
            curr = arr.pop()
            if curr in ["+", "-", "*", "/"]:
                op1 = int(stk.pop())
                op2 = int(stk.pop())
                if curr == "+":
                    res = op1 + op2
                elif curr == "-":
                    res = op2 - op1
                elif curr == "*":
                    res = op1 * op2
                else:
                    res = int(op2 / op1)
                stk.append(str(res))
            else:
                stk.append(curr)
    

        return int(stk.pop())


# Time: O(a), a is number of elements in arr
# Space: O(a), a is space used for the stack array.