import math

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        if len(roads)==0:
            return(0)
        
        adj = defaultdict(list)
        node_count = len(roads)+1

        for s,c in roads:
            adj[s].append(c)
            adj[c].append(s)

        visited = set()
        self.ans = 0
        
        def dfs(node):

            visited.add(node)
            pax = 1

            for nei in adj[node]:
                if nei not in visited:
                    passenger_moved = dfs(nei)
                    self.ans+= math.ceil(passenger_moved/seats)
                    pax += passenger_moved
    
            return(pax)


        total_pax = dfs(0)
        return(self.ans)

