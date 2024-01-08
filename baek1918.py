notation = "(" + input() + ")"

stack = []
i = 0
while i < len(notation):
    nowChar = notation[i]
    if nowChar == "(" or nowChar == "*" or nowChar == "/" or nowChar == "+" or nowChar == "-":
        stack.append(nowChar)
    elif nowChar == ")":
        smallStack = []
        while stack[-1] != "(":
            smallStack.append(stack.pop())
        nowChar = smallStack.pop()
        while smallStack:
            operand = smallStack.pop()
            number = smallStack.pop()
            nowChar = nowChar + number + operand
        stack.pop()
        stack.append(nowChar)
    else:
        if stack:
            prevChar = stack[-1]
            if prevChar == "*" or prevChar == "/":
                operand = stack.pop()
                number = stack.pop()
                nowChar = number + nowChar + operand
        stack.append(nowChar)
    i += 1

print(stack.pop())