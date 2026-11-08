class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        - have a hashmap that stores poitions and have how much money it costs to get there
        - if a cheaper way is fond, update
        - always start by adding the starting ditance val to the new distance
        - also keep track of k, first check to make sure k is valid


        have a ditance map:
        iterate thru k + 1 times
        make a new copy of hashmap differecens
        if the starting distacne is in distance (within +1) then update val if new distacne to be the min in both



        '''


        dist = [float("inf")] * n
        dist[src] = 0

        for _ in range(k+1):
            new_dist = dist.copy()
            for u, v, price in flights:
                if dist[u] == float("inf"):
                    continue
                new_dist[v] = min(new_dist[v], dist[u]+price)
            dist = new_dist
        return -1 if dist[dst] == float("inf") else dist[dst]