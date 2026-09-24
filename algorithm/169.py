class Solution:
    def majorityElement(self,nums:list[int]):
        a={}
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for k,v in a.items():
            if v > len(nums)//2:
                return k
sol=Solution()
print(sol.majorityElement([3,3,2]))
