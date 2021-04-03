import math
class Graph:
  
    def __init__(self, V):
        self.V = V 
        self.adj = [[] for i in range(V)]
      
    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def DFS(self, v, visited):
        visited[v] = True
        
        i = 0
        while i != len(self.adj[v]):
            if (not visited[self.adj[v][i]]): 
                self.DFS(self.adj[v][i], visited)
            i += 1
    
    def isConnected(self):
        visited = [False] * self.V
        
        self.DFS(0, visited) 
      
        for i in range(1, self.V):
            if (visited[i] == False): 
                return False
      
        return True
    
    def isBridge(self, u, v):
          
        indV = self.adj[u].index(v)
        indU = self.adj[v].index(u)
        del self.adj[v][indU]
        del self.adj[u][indV]
      
        res = self.isConnected() 
        
        self.addEdge(u, v) 
        
        return (res == False)

    def isvisitedCount(self,u,v):
        count=0

        indV = self.adj[u].index(v)
        indU = self.adj[v].index(u)
        del self.adj[v][indU]
        del self.adj[u][indV]

        visited = [False] * self.V
        self.DFS(0, visited) 
      
        for i in range(1, self.V):
            if (visited[i] == False): 
                count+=1

        self.addEdge(u, v) 

        return count

    

n,m=map(int,input().strip().split())  
g= Graph(n)
edges=[]
for _ in range(m):
    input_u,input_v = map(int,input().strip().split())  
    u,v = input_u-1,input_v-1
    g.addEdge(u,v)
    edges.append([u,v])

bride_edges=[]
bridge_edge_count=0
for i in range(m):
    u,v = edges[i][0],edges[i][1]
    if g.isBridge(u,v):
        bridge_edge_count+=1
        bride_edges.append([u,v])
x_win_count=0
y_win_count=0
if bridge_edge_count==0:
    print(0,0)
    quit()

else:
    for j in range(len(bride_edges)):
        u,v=bride_edges[j][0],bride_edges[j][1]
        count = g.isvisitedCount(u,v)
        if (count%2==0 and (n-count)%2==0):
            x_win_count+=1
        else:
            y_win_count+=1

p_x=x_win_count
p_y=y_win_count
q=bridge_edge_count

x_gcd=math.gcd(p_x,q)
y_gcd=math.gcd(p_y,q)

p_x_co = p_x//x_gcd
q_x_co = q//x_gcd

p_y_co = p_y//y_gcd
q_y_co = q//y_gcd


 
 
def modInverse(a, m):
    return power(a, m - 2, m)
 
 
def power(x, y, m):
 
    if (y == 0):
        return 1
    p = power(x, y // 2, m) % m
    p = (p * p) % m
 
    if(y % 2 == 0):
        return p
    else:
        return ((x * p) % m)
 
 

print(p_x_co*modInverse(q_x_co,(10**9)+7),p_y_co*modInverse(q_y_co,(10**9)+7))


