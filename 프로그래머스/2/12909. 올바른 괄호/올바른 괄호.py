def solution(s):
    stack=[]
    for x in s:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0