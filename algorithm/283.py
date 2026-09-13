def moveZeroes(nums:list[int]):
    a=0
    for b in range(len(nums)):
        if nums[b] != 0:
            nums[a],nums[b]=nums[b],nums[a]
            a+=1
    return nums

print(moveZeroes([0,4,7,23,6,1,0,5,0,1,0]))