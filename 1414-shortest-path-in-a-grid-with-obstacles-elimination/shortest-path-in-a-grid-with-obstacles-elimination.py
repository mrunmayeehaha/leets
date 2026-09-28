from collections import deque

class Solution:
    def shortestPath(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        queue = deque([(0, 0, k, 0)])
        visited = {(0, 0, k)}

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:
            r, c, remaining, steps = queue.popleft()

            if r == m - 1 and c == n - 1:
                return steps

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:

                    new_remaining = remaining

                    if grid[nr][nc] == 1:
                        new_remaining -= 1

                    if new_remaining < 0:
                        continue

                    state = (nr, nc, new_remaining)

                    if state in visited:
                        continue

                    visited.add(state)

                    queue.append(
                        (nr, nc, new_remaining, steps + 1)
                    )

        return -1