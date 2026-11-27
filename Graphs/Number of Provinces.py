# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

# EX1:
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# EX2:
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3

class Solution:
    def findCircleNum(self, isConnected: List[List[int]])-> int:
        
        def dfs(i):
            self.visited.add(i)
            for j in range(n):
                if isConnected[i][j] and j not in self.visited:
                    dfs(j)
            return
        
        self.visited = set()
        province = 0
        n = len(isConnected)
        for i in range(n):
            if i not in self.visited:
                province += 1
                dfs(i)
        return province