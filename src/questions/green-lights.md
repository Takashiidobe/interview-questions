You are trying to drive from the top left of a city to the bottom right corner.
Your car can only move to directly to the right or directly down.
The city roads are stored in a 2d matrix of size m*n.
The values at `grid[i][j]` represent the time when that traffic light will turn green (meaning you can access that position).
Return the minimum time it takes to reach the bottom right hand corner.

```
[
 [1, 2, 3, 4],
 [2, 2, 2, 1],
 [4, 3, 5, 2]
]

result = 2
```

What happens if you can go 4-dimensionally?

```
[
 [1, 1, 1, 9],
 [9, 9, 1, 9],
 [1, 1, 1, 9],
 [1, 9, 9, 9],
 [1, 1, 1, 1]
]

result = 1
```

Solutions:

```py
def bfs(grid):
    q = deque([((0, 0), grid[0][0])])
    m = len(grid)
    n = len(grid[0])

    def inbounds(i, j):
        nonlocal m, n
        return i >= 0 and i < m and j >= 0 and j < n

    curr_min = float('inf')
    visited = {(i, j): float('inf') for i in range(m) for j in range(n)}

    while q:
        print(q)
        ((i, j), curr_time) = q.popleft()
        if i == m - 1 and j == n - 1:
            curr_min = min(curr_min, curr_time)
            continue
        candidates = []
        if inbounds(i + 1, j):
            down_cost = max(curr_time, grid[i + 1][j])
            if down_cost < visited[(i + 1, j)]:
                candidates.append(((i + 1, j), down_cost))
                visited[(i + 1, j)] = down_cost
        if inbounds(i, j + 1):
            right_cost = max(curr_time, grid[i][j + 1])
            if right_cost < visited[(i, j + 1)]:
                candidates.append(((i, j + 1), right_cost))
                visited[(i, j + 1)] = right_cost

        q.extend(candidates)

    return curr_min
grid = [
 [1, 2, 4, 4],
 [2, 2, 4, 1],
 [4, 3, 5, 2]
]

from collections import deque

def bfs(grid):
    q = deque([((0, 0), grid[0][0])])
    m = len(grid)
    n = len(grid[0])

    def inbounds(i, j):
        nonlocal m, n
        return i >= 0 and i < m and j >= 0 and j < n

    curr_min = float('inf')

    while q:
        ((i, j), curr_time) = q.popleft()
        if i == m - 1 and j == n - 1:
            curr_min = min(curr_min, curr_time)
            continue
        candidates = []
        if inbounds(i + 1, j):
            candidates.append(((i + 1, j), max(curr_time, grid[i + 1][j])))
        if inbounds(i, j + 1):
            candidates.append(((i, j + 1), max(curr_time, grid[i][j + 1])))

        q.extend(candidates)

    return curr_min

print(bfs(grid))
```

```py
grid2 = [
 [1, 1, 1, 9],
 [9, 9, 1, 9],
 [1, 1, 1, 9],
 [1, 9, 9, 9],
 [1, 1, 1, 1]
]

from collections import deque

def bfs(grid):
    q = deque([((0, 0), grid[0][0])])
    m = len(grid)
    n = len(grid[0])
    visited = {(i, j): float('inf') for i in range(m) for j in range(n)}

    def inbounds(i, j):
        nonlocal m, n
        return i >= 0 and i < m and j >= 0 and j < n

    while q:
        ((i, j), curr_time) = q.popleft()
        candidates = []
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            new_i, new_j = di + i, dj + j
            new_loc = (new_i, new_j)
            if inbounds(*new_loc) and curr_time < visited[new_loc]:
                visited[new_loc] = min(visited[new_loc], max(curr_time, grid[new_i][new_j]))
                candidates.append((new_loc, max(curr_time, grid[new_i][new_j])))

        q.extend(candidates)

    return visited[(m - 1, n - 1)]

print(bfs(grid2))
```

```py
grid = [
 [1, 4, 3, 4],
 [5, 2, 2, 1],
 [4, 3, 5, 2]
]

from queue import PriorityQueue

def getMinTime(matrix):
    posLowDict = {}
    pq = PriorityQueue()
    if len(matrix) == 0:
        return 0
    pq.put((matrix[0][0], 0, 0))
    while pq:
        print(pq)
        pos, x, y = pq.get()
        if cur[1] == len(matrix[0])-1 and cur[2] == len(matrix)-1:
            return cur[0]
        if cur[1] + 1 < len(matrix[0]):
            curLowTime = max(cur[0], matrix[cur[2]][cur[1]+1])
            if (cur[1]+1, cur[2]) in posLowDict and curLowTime >= posLowDict[(cur[1]+1, cur[2])]:
                continue
            posLowDict[(cur[1]+1, cur[2])] = curLowTime
            pq.put((curLowTime, cur[1]+1, cur[2]))
        if cur[2] + 1 < len(matrix):
            pq.put((max(cur[0], matrix[cur[2]+1][cur[1]]), cur[1], cur[2]+1))

from collections import deque

def bfs(grid):
    q = deque([((0, 0), grid[0][0])])
    m = len(grid)
    n = len(grid[0])

    def inbounds(i, j):
        nonlocal m, n
        return i >= 0 and i < m and j >= 0 and j < n

    curr_min = float('inf')

    while q:
        print(q)
        ((i, j), curr_time) = q.popleft()
        if i == m - 1 and j == n - 1:
            curr_min = min(curr_min, curr_time)
            continue
        candidates = []
        if inbounds(i + 1, j):
            candidates.append(((i + 1, j), max(curr_time, grid[i + 1][j])))
        if inbounds(i, j + 1):
            candidates.append(((i, j + 1), max(curr_time, grid[i][j + 1])))

        q.extend(candidates)

    return curr_min

print(getMinTime(grid))
print(bfs(grid))
```
