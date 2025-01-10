def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    ...  # TODO реализовать проверку скобочной группы

    stack = []
    flag = True
    for elem in brackets_row:
        if elem == '(':
            stack.append(elem)
        elif elem == ')':
            if len(stack) == 0:
                flag = False
                break
            elif stack[-1] == '(':
                stack.pop()

    if (flag and len(stack) == 0):
        return True
    else:
        return False

if __name__ == '__main__':
    print(check_brackets("()()()"))  # True
    print(check_brackets(''))
    print(check_brackets(")("))  # False
    print(check_brackets('((())')) # False

