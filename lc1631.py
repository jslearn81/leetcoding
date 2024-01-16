class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        if not heights:
            return 0

        #Graph comes with weight, so djikstra

        nrow, ncol = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        min_h = [(0,0,0)]
        max_effort = 0


        while len(min_h)>0:
            
            cost, i, j = heapq.heappop(min_h)
            max_effort = max(max_effort, cost)
            if i==nrow-1 and j==ncol-1:
                return max_effort
            
            visited.add((i,j))

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0<=ni<nrow and 0<=nj<ncol and (ni,nj) not in visited:
                    heapq.heappush(min_h, (abs(heights[ni][nj]-heights[i][j]), ni, nj))
