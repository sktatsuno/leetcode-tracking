from heapq import heappop, heappush


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        # sort tasks
        task_list = [
            (enqueue, processing, idx)
            for idx, (enqueue, processing) in enumerate(tasks)
        ]

        # enqueue time, proccessing time, original index
        task_list.sort()
        res = []
        # min heap to choose shortest task
        available_tasks = []
        t = 0
        i = 0

        while len(res) < len(task_list):
            # heap is empty, tasks still to process
            if not available_tasks:
                t = max(t, task_list[i][0])

            # iterate through tasks
            # add to heap if t is enqueue time
            while i < len(task_list) and task_list[i][0] <= t:
                heappush(available_tasks, (task_list[i][1], task_list[i][2]))
                i += 1

            p_time, original_i = heappop(available_tasks)
            res.append(original_i)
            t += p_time

        return res
