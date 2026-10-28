class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        iterating through the edges list
        and in a hashet, have the keys be the edges and the values be the nodes theyre connected to

        for each iteration:
            - add edges to hashset if not alrdy in
            - have hashset be set()s
            - for each edge update values by adding edges into set()
            * have the values be a set

            {0: 0, 1, 2}
            {1: 0, 1, 2}
            {2: 0, 1, 2}
            {3: 3, 4}
            {4: 3, 4}

            loop thu hashset and check if values equal to last one, if not update count, return counter


        dfs
        1. build an adjcency list from the edges
        2. iterate thru each node
        3. for every unvisited node start dfs, marking all connected nodes as visited
        4. each dfs update count by 1
        '''
        count = 0
        adjlist = {}
        visited = set()
        def dfs(node, adjlist, visited, count):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adjlist[node]:
                dfs(neighbor, adjlist, visited, count)
            
            return count
        

        for n1, n2 in edges:
            if n1 not in adjlist:
                adjlist[n1] = []
            if n2 not in adjlist:
                adjlist[n2] = []
            adjlist[n1].append(n2)
            adjlist[n2].append(n1)
        

        for node in adjlist:
            if node not in visited:
                dfs(node, adjlist, visited, count)
                
                count += 1
        
        if len(visited) < n:
            count += (n-len(visited))
        return count










