class Solution:
    def solution(self, grid):
        m, n = len(grid), len(grid[0])
        roots = {(y, x): (y, x) for y in range(m) for x in range(n) if grid[y][x] == "1"}
        self.count = len(roots)

        def find(p):
            if p != roots[p]:
                return find(roots[p])
            return p

        def union(p, q):
            p, q = find(p), find(q)
            if p != q:
                if p < q:
                    roots[p] = q
                else:
                    roots[q] = p
                self.count -= 1

        for y in range(m):
            for x in range(n):
                if grid[y][x] == "1":
                    if x + 1 < m and grid[y][x+1] == "1":
                        union((y,x),(y,x+1))
                    if y + 1 < n and grid[y+1][x] == "1":
                        union((y,x),(y+1,x))

        return self.count
