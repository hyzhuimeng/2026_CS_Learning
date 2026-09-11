def isPalindrome(s:str):
    a="".join(i.lower()for i in s if i.isalnum())
    left=0
    right=len(a)-1
    while left < right:
        if a[left]==a[right]:
            left+=1
            right-=1
        else:
            return False
    return True
print(isPalindrome("A man Is ,, love"))
print(isPalindrome("a Man Nam A"))
#时间复杂度：o(n)
#空间复杂度：o(n)
