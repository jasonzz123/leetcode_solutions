class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]

        start = 0
        end = len(nums)-1
        while start + 1 < end:
            while start < len(nums)-1 and nums[start] == nums[start+1]:
                start += 1
            while end > 0 and nums[end] == nums[end-1]:
                end -= 1
            mid = start + (end-start)//2
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid
        return min(nums[start], nums[end])
