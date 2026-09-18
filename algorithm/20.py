def isValid(s:str):
    stack=[]
    dict={")":"(","]":"[","}":"{"}
    for char in s:
        if char is dict.values:
            stack.append(char)
        elif not stack or stack.pop() != dict.keys:
            return False
    return len(stack)==0
print(isValid("{}([]){}"))
