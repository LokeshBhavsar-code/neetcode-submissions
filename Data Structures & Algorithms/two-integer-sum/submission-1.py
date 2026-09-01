class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}

        for i in range(len(nums)):
            required=target -nums[i]

            if required in hash:
                return [hash[required],i]
            
            hash[nums[i]]=i