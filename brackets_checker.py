def brackets_checker(expression):
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if stack and brackets[stack[-1]] == char:
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    return True