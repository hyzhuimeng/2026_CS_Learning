def canConstruct(ransomNote:str,magazine:str):
    a={}
    for i in magazine:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
    b={}
    for n in ransomNote:
            if n in b:
                b[n]+=1
            else:
                b[n]=1
    for k,v in b.items():
         if k not in a or v > a[k]:
              return False
         else:
              return True
print(canConstruct("aoo","aoaoaodjaoc",))
print(canConstruct("caoipyfudahc","sdhjaiopc"))
#时间复杂度：O(n)
#空间复杂度：o(m+n)
        