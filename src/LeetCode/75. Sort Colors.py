class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        t = True
        while t:
            t = False
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    t = True
            i = i + 1
        return nums