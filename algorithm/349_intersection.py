def intersection(nums1:list[int],nums2:list[int]) -> list[int]:
    return list(set(nums1) & set(nums2))
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
intersection_result = intersection(nums1, nums2)
print(intersection_result) 
#时间复杂度：o(n)
#空间复杂度：o(n)