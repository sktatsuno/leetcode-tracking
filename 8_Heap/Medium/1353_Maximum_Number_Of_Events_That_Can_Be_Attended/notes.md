Read through entire problem and test cases before starting to form approach I could've saved a bunch of time on figuring out that you only need to attend one day of each event

Don't forget you can simply use heap[0] to look at top of heap without popping

First attempt approach
- I couldn't figure out if I needed to sort the initial events array first.  
- If sort by start date initially do not need start date in heap at all
- I understood I needed to pop events with earliest end dates off the heap, but didn't get to the realization that you're only pushing events with valid start dates to the heap. The heap represents events with active start date

Don't do heap.heappush because the heap is an argument of heappush() function. Same with all the heapq methods

Second attempt with help
- When you do a while i < _____ loop remember to increment i to continue loop or will get TLE
- Also I mistakenly incremented i when removing end dates from the heap