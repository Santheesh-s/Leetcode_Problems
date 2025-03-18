class Solution(object):
    def mostFrequentEven(self, nums):
        ls=sorted(list(set(i for i in nums if i%2==0)))
        ls1=[nums.count(i) for i in ls]
        return ls[ls1.index(max(ls1))] if len(ls1) else -1
