class Solution:
    def search(self,nums:list[int],target:int):
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
        return -1
sol=Solution()
print(sol.search([1,3,5,6,7,8],6))
print(sol.search([1,2,5,8,9,4],0))