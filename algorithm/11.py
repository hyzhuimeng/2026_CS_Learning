def maxArea(height:list[int]):
    i,j,res=0,len(height)-1,0
    while i < j:
        if height[i] < height[j]:
            res=max(res,height[i]*(j-i))
            i+=1
        else:
            res=max(res,height[j]*(j-i))
            j-=1
    return res
print(maxArea([2,6,3,76,8,3]))
#时间复杂度：O(n)
#空间复杂度：o(1)
