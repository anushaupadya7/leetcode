# Last updated: 19/09/2025, 00:17:02
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent={}
        rank={}

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            rootX,rootY=find(x),find(y)
            if rootX==rootY:
                return False
            if rank[rootX]>rank[rootY]:
                parent[rootY]=rootX
            elif rank[rootX]<rank[rootY]:
                parent[rootX]=rootY
            else:
                parent[rootY]=rootX
                rank[rootX]+=1
            return True


        for u,v in edges:
            if u not in parent:
                parent[u]=u
                rank[u]=0
            if v not in parent:
                parent[v]=v
                rank[v]=0
            if not union(u,v):
                return [u,v]