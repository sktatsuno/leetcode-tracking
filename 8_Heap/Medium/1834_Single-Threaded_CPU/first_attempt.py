from heapq import heappop, heappush


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        # sort tasks
        for i in range(0, len(tasks)):
            tasks[i].append(i)
        # enqueue time, proccessing time, original index
        tasks.sort()
        res = []
        # min heap to choose shortest task
        available_tasks = []
        t = 0
        i = 0

        while len(res) < len(tasks):
            # heap is empty, tasks still to process
            if not available_tasks:
                t = max(t, tasks[i][0])

            # iterate through tasks
            # add to heap if t is enqueue time
            while i < len(tasks) and tasks[i][0] <= t:
                heappush(available_tasks, [tasks[i][1], tasks[i][2]])
                i += 1

            p_time, original_i = heappop(available_tasks)
            res.append(original_i)
            t += p_time

        return res
