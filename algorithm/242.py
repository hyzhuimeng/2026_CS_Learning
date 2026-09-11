def isAnagram(s:str,t:str):
    a={}
    b={}
    for i in s:
        if i in a:
            a[i] +=1
        else:
            a[i] =1
    for n in t:
        if n in b:
            b[n]+=1
        else:
            b[n]=1
    if a==b:
        return True
    else:
        return False

print(isAnagram("common","iaoch"))
print(isAnagram("anagram","nagaram"))