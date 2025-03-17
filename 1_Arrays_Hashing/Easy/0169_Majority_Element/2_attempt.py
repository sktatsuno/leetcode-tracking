from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # To do it in O(1) space that would mean not counting for each
        # different element
        # We would need to use one count for both elements
        # Assume majority element always exists in array
        counter = 0
        candidate = nums[0]

        for num in nums:
            if num == candidate:
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                candidate = num
                # the -1 of the new candidate switches to 1
                counter = 1
        # What if the majority element does not always exist
        # Well if majority element doesnt exist then the count would be 0
        if counter == 0:
            return None

        return candidate


solution = Solution()
print(solution.majorityElement([3, 2, 3]))
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(solution.majorityElement([2, 2, 1, 1]))
