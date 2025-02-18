class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()

        tasks.sort(reverse=True)
        
        min_time = 0
        task_index = 0

        for i in range(len(processorTime)):
            max_task = max(tasks[task_index:task_index+4])  
            min_time = max(min_time, processorTime[i] + max_task)
            task_index += 4  
        
        return min_time
