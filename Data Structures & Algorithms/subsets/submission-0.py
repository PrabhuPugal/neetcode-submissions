class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def recurrence(nums,i,res,subarray):
            if i == len(nums):
                res.append(list(subarray))
                return
            
            recurrence(nums, i+1, res, subarray)
            subarray.append(nums[i])
            recurrence(nums,i+1, res, subarray)
            subarray.pop()

        def subset(nums):
            subarray=[]
            res=[]
            recurrence(nums, 0, res, subarray)
            return res
        
        return subset(nums)