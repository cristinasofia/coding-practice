class Solution(object):
    def findCircleNum_BFS(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        count = 0
        visit = [0] * len(M)
        
        q = []
        
        for i in range(len(M)):
            if M[i][i] == 1 and not visit[i]:
                q.append(i)
                while q:
                    j = q.pop(0)
                    visit[j] = 1
                    for k in range(len(M)):
                        if M[j][k] == 1 and not visit[k]:
                            q.append(k)
                count += 1
        return count
    
    def findCircleNum_DFS(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        count = 0
        visit = [0] * len(M)
        
        def dfs(j):
            visit[j] = 1
            
            for k in range(len(M)):
                if M[j][k] == 1 and not visit[k]:
                    dfs(k)
        
        for i in range(len(M)):
            if M[i][i] == 1 and not visit[i]:
                dfs(i)
                count += 1
        return count