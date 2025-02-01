class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k == 0 or k % len(nums) == 0:
            return
        tk = k % len(nums)
        temp = nums[-tk:]
        nums[tk:] = nums[:-tk]
        nums[:tk] = temp
        return
