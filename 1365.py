# 暴力
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            tem = 0
            for j in nums:
                if i!= j:
                    if i > j:tem+=1
            res.append(tem)
        return res

# 先排序，然后找出第一次出现的index 解决重复出现的情况
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nn = sorted(nums)
        dic = {}
        for i,n in enumerate(nn):
            if n not in dic:
                dic[n] = i
        nn = []
        for n in nums:
            nn.append(dic[n])
        return nn
