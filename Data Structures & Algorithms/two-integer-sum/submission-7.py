class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter={}
        for i in range(len(nums)):
            required=target-nums[i]
            if required in counter:
                return [counter[required],i]
            counter[nums[i]]=i

