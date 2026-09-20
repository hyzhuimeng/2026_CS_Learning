class Solution:
    def lengthOfLongestSubstring(self,s:str):
        a=set()
        left=0
        max_len=0
        for right in range(len(s)):
            char = s[right]
            while char in a:
                a.discard(s[left])
                left += 1
            a.add(char)
            max_len = max(max_len,right-left+1)
        return max_len
sol=Solution()
print(sol.lengthOfLongestSubstring("WIOFHAFUHQOGFWKJHLIAHFOWUTGIFGLK"))