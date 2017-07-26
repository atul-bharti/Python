from Stack import Stack
import re
def is_balanced(p_str):
    if p_str is None or p_str == '':
        return True
    p_dict = {'(':')'}
    stack = Stack()
    newStr = p_str.replace(' ','')
    newStr = re.sub(r'[a-z]*','',newStr)

    for s in newStr :

        if not stack.is_empty() and s == p_dict[stack.peek()]:
            stack.pop()
        else:
            stack.push(s)

    if stack.is_empty():
        return True
    else:
        return False



def is_balanced_generic(p_str):
    if p_str is None or p_str == '':
        return True
    p_dict = {'(':')','[':']','{':'}',')':'',']':'','}':''}
    stack = Stack()
    newStr = p_str.replace(' ','')
    newStr = re.sub(r'[a-z]*','',newStr)

    for s in newStr :

        if not stack.is_empty() and s == p_dict[stack.peek()]:
            stack.pop()
        else:
            stack.push(s)

    if stack.is_empty():
        return True
    else:
        return False


print(is_balanced_generic('{[)(]}{}'))

