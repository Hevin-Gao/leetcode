# 即使使用滑动窗口也有for循环的思想
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        t = False
        i = 0
        tem = 0
        for j in range(len(nums)):
            tem+=nums[j]
            while tem >= target and i <= j:
                t = True
                res = min(res,j-i+1)
                tem-=nums[i]
                i+=1
        if t==False:return 0
        return res
