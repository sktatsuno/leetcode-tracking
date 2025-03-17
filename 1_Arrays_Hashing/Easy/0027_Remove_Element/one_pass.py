from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k represents position next non-target should go
        k = 0

        for i in range(len(nums)):
            # If not target then move to k, then increment k
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        # Return number of non-targets
        print(nums)
        return k
