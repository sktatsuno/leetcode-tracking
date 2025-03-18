from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Only a max of 2 elements could show up
        # How can we solve in linear time and O(1) space?
        # Need to use voting algorithm, but it is tracking more than 2 options
        if not nums:
            return []

        counter_1, counter_2 = 0, 0
        candidate_1, candidate_2 = None, None
        result = []
        threshold = len(nums) // 3

        # First pass: find potential candidates
        for num in nums:
            if num == candidate_1:
                counter_1 += 1
            elif num == candidate_2:
                counter_2 += 1
            # if one of candidates is surpassed replace
            # and reset counter
            elif counter_1 == 0:
                candidate_1, counter_1 = num, 1
            elif counter_2 == 0:
                candidate_2, counter_2 = num, 1
            else:
                counter_1 -= 1
                counter_2 -= 1

        # Second Pass: Validate candidates because the potential candidates
        # are not guaranteed to be majority
        counter_1, counter_2 = 0, 0
        for num in nums:
            if num == candidate_1:
                counter_1 += 1
            elif num == candidate_2:
                counter_2 += 1

        # Return only valid candidates
        if counter_1 > threshold:
            result.append(candidate_1)
        if counter_2 > threshold:
            result.append(candidate_2)

        return result
