def IsValid(s):
    stack = []

    mapping = {")": "(",
               "]": "[",
               "}": "{"}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'

            if mapping[char] != top_element:
                return False

        else:
            stack.append(char)

    return not stack


def paren(s):
    stack = []
    this_dict = {
        '}': '{',
        ')': '(',
        ']': '['
    }

    if not s:
        return True

    for i in s:
        if i in '({[':
            stack.append(i)
        elif i in ')]}':
            if stack != [] and this_dict[i] == stack.pop():
                pass
            else:
                return False
        else:
            pass

    return not stack


if __name__ == '__main__':
    # print(IsValid("{{({})}}"))
    # print(IsValid("(((((((((("))
    # print(IsValid("({})[]"))
    print(IsValid("{[]}"))
    print(paren('{[()]}()'))
