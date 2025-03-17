from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[j] == val:
                j -= 1
            elif nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            else:
                i += 1
        if nums[i] == val:
            return i
        return i + 1
