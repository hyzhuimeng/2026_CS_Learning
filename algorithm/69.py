class Solution:
    def mySqrt(self,x:int):
        left=0
        right=x
        while left<right:
            mid=left+(right-left)//2
            if mid**2 < x:
                left=mid+1
            elif mid**2 > x:
                right=mid
            else:
                return mid
        return left-1 if left*left>x else left
sol=Solution()
print(sol.mySqrt(8))
print(sol.mySqrt(2))
print(sol.mySqrt(1))
print(sol.mySqrt(0))
