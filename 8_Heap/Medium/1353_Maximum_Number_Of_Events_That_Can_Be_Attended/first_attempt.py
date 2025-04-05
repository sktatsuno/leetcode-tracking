from heapq import heappush, heappop
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        heap = []
        d = 1
        max_end_date = 0
        res = 0

        # Push end date first to min heap to attend events ending sooner
        for event in events:
            start_date, end_date = event[0], event[1]
            max_end_date = max(max_end_date, end_date)
            heappush(heap, (end_date, start_date))

        # For each day attend the earliest available day of the event
        # When attend event increment result and increment day
        # There may be events you cannot attend that need to be popped off heap without incrementing
        while d <= max_end_date:
            end_date, start_date = heappop(heap)

            # Keep popping until can attend
            while d < start_date or d > end_date:
                end_date, start_date = heap.heappop(heap)
                # Do I need to add back events haven't attended if end date still > d?

    # Once attend the event one day don't need anymore

    # If it's a multiday event you only need to attend one day
    # So we want to go to the earliest day we can go to?
    # If two events same time you want to attend shorter one first
