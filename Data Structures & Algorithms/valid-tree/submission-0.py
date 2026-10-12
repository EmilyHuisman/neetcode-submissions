class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # build up adjaceny matrix
        # a cycle is if the child on two verticies also has an edge between
        # breadth first search - if you see smth in visited again - false
        # if in visited but not eaul to parent
        if len(edges) > n-1:
            return False

        adjacencyList = [[] for _ in range(n)]
        for x, y in edges:
            adjacencyList[x].append(y)
            adjacencyList[y].append(x)
        
        
        queue = deque()
        visited = set()
        queue.append((0, -1))
        visited.add(0)

        
        while queue:
            node, parent = queue.popleft()

            for x in adjacencyList[node]:
                if x == parent:
                    continue
                if x in visited:
                    return False
                visited.add(x)
                queue.append((x, node))

        return len(visited) == n














