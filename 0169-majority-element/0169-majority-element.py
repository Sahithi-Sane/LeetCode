class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
    
        n = len(nums)
        for num, count in counts.items():
            if count > n // 2:
                return num
        