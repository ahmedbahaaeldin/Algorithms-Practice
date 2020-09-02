    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        if root.children == []:
            return 1
        answer = 0
        def dfs(graph,depth):
            nonlocal answer
            depth += 1
            if not graph.children:
                answer = max(answer,depth)
                return
            for children in graph.children:
                dfs(children,depth)
            return answer
        return dfs(root, 0)
