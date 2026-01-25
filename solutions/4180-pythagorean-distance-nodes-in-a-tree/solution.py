from collections import deque
class Solution(object):
    def specialNodes(self, n, edges, x, y, z):
        adj=[[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def get_dist(start):
            dist=[-1]*n
            dist[start]=0
            queue=deque([start])
            while(queue):
                cur=queue.popleft()
                for neighbour in adj[cur]:
                    if dist[neighbour]==-1:
                        dist[neighbour]=dist[cur]+1
                        queue.append(neighbour)
            return dist

        dx=get_dist(x)
        dy=get_dist(y)
        dz=get_dist(z)

        sp=0
        for i in range(n):
            dists=sorted([dx[i],dy[i],dz[i]])
            a,b,c=dists[0],dists[1],dists[2]

            if a>=0 and (a*a+b*b==c*c):
                sp+=1
        return sp
