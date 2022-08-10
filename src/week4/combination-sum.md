# Combination Sum

## Solution

```py
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def dfs(i, remaining, curr):
            if remaining == 0:
                ans.append(curr.copy())
                return
            if remaining < 0 or i >= n:
                return
            candidate = candidates[i]
            curr.append(candidate)
            dfs(i, remaining - candidate, curr)
            curr.pop()
            dfs(i + 1, remaining, curr)

        dfs(0, target, [])

        return ans
```
