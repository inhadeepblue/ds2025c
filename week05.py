def is_vaild_brackets(expression : str) -> bool:  # type hint
    stack = []
    brackets = {')':'(', '}':'{', ']':'[' }

    for letter in expression:
        if letter in brackets.values():
            stack.append(letter)
        if letter in brackets.keys():
            if not stack or stack.pop() != brackets[letter]:
                return False
    return not stack

print(is_vaild_brackets("([2+3])"))
print(is_vaild_brackets("(2+{3*9})"))
print(is_vaild_brackets("(2+(3*9)"))  # 스택에 여는 소괄호가 하나 남아 있어서 False
print(is_vaild_brackets(")2+(3*9)("))