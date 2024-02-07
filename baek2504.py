inString = input()

wrong = False
stack = []
for now in inString:
    if now == '(':
        stack.append(now)
    elif now == '[':
        stack.append(now)
    elif now == ')':
        if len(stack) >= 1:
            if stack[-1] == '(':
                stack.pop()
                stack.append(2)
            elif stack[-1] != '[':
                cache = 0
                while stack and not stack[-1] in ['(', '[']:
                    cache += stack.pop()
                if stack and stack[-1] == '(':
                    stack.pop()
                    cache *= 2
                    stack.append(cache)
                else:
                    wrong = True
                    break
            else:
                wrong = True
                break
        else:
            wrong = True
            break
    elif now == ']':
        if len(stack) >= 1:
            if stack[-1] == '[':
                stack.pop()
                stack.append(3)
            elif stack[-1] != '(':
                cache = 0
                while stack and not stack[-1] in ['(', '[']:
                    cache += stack.pop()
                if stack and stack[-1] == '[':
                    stack.pop()
                    cache *= 3
                    stack.append(cache)
                else:
                    wrong = True
                    break
            else:
                wrong = True
                break
        else:
            wrong = True
            break

if wrong:
    print(0)
else:
    print(sum(stack))
