def twoSum(numbers:list[int],target:int):
    left=0;
    right=len(numbers)-1
    while numbers[left]+numbers[right] != target:
        if numbers[left]+numbers[right] > target:
            right-=1
        else:
            left+=1
    return [left+1,right+1]
print(twoSum([2,4,7,8],9))