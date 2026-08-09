<h2><a href="https://leetcode.com/problems/task-scheduler">Task Scheduler</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## approach:

- use a max heap to always pick the task that has been used the most number of times.
- First, count how many times each task appears.
- Store these frequencies in a max heap. Since Python has a min heap, I store them as negative values.
- At each time interval, pick the task with the highest remaining frequency.
- After running a task, it cannot be used again until n intervals have passed so keep it in a queue along with the time when it becomes available again.
- If no task is currently available the CPU stays idle.
- Once a task's cooldown is over put it back into the heap.
- Continue until there are no remaining tasks.

- Time complexity: O(n logK)
- Space complexity: O(K)
