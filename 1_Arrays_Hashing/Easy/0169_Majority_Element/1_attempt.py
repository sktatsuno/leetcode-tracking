from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # To do it in O(1) space that would mean not counting for each
        # different element
        # We would need to use one count for both elements
        # Assume majority element always exists in array
        count = 1
        candidate = nums[0]
        for num in nums:
            if num == candidate:
                count += 1
            else:
                count -= 1
            if count < 0:
                candidate = num

        return candidate


# What if the majority element does not always exist
# Well if majority element doesnt exist then the count would be 0 right?
