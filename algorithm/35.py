class Solution:
    def searchInsert(self,nums:list[int],target:int):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                return mid
        return left
sol=Solution()
print(sol.searchInsert([1,3,5,6,7,8],6))
print(sol.searchInsert([1,2,5,8,9,4],0))