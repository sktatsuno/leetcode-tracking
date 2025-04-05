from heapq import heappush, heappop
from typing import List


class Solution:
    def max_events(self, events: List[List[int]]) -> int:
        # Sort events by start date
        events.sort()

        heap = []
        d = 0
        res = 0
        # Track number of events gone through
        i = 0

        # Go through events by day
        # While there are still events in the start list or in the remaining
        # active events heap
        while i < len(events) or heap:
            # Skip to next event's start date if no dates in heap
            # No point in going through each day if there are no start days
            # for them
            if not heap:
                d = events[i][0]

            # Add all events that start on or before the current day
            while i < len(events) and events[i][0] <= d:
                # Min Heap is used to retrieve earliest end date
                # We only care about number of events attended we don't need
                # to track which events attended
                heappush(heap, events[i][1])
                i += 1

            # Remove events that are no longer available
            while heap and heap[0] < d:
                heappop(heap)

            # Attend one event if possible
            # The other events stay in heap because they can potentially still
            # be attended later
            if heap:
                heappop(heap)
                res += 1

            # Move on to the next day
            d += 1

        return res


s = Solution()
print(s.max_events([[1, 2], [2, 3], [3, 4]]),
      s.max_events([[1, 2], [2, 3], [3, 4]]) == 3)
print(s.max_events([[1, 2], [2, 3], [3, 4], [1, 2]]),
      s.max_events([[1, 2], [2, 3], [3, 4], [1, 2]]) == 4)
