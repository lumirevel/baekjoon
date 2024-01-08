notation = "(" + input() + ")"

stack = []
for nowChar in notation:
    if nowChar == ")":
        smallStack = []
        while stack[-1] != "(":
            smallStack.append(stack.pop())
        nowChar = smallStack.pop()
        while smallStack:
            operand = smallStack.pop()
            number = smallStack.pop()
            nowChar = nowChar + number + operand
        stack.pop()
    if stack:
        if nowChar != "(":
            prevChar = stack[-1]
            if prevChar == "*" or prevChar == "/":
                operand = stack.pop()
                number = stack.pop()
                nowChar = number + nowChar + operand
    stack.append(nowChar)

print(stack.pop())