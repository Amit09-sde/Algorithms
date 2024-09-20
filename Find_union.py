
class uf:
    l = []
    def __init__(self,n):
       
        for i in range(n):
            self.l.append(i)
            
    def connected(self,p,q):
        return self.l[p]==l[q]
        
    def union(self,p,q):
        pid = self.l[p]
        qid = self.l[q]
        
        for i in range(len(self.l)):
            if self.l[i] == pid:
                self.l[i] = qid
                
                
    def show(self):
        print(self.l)
                

n = int(input())
ob = uf(n)

for _ in range(n):
    x,y=map(int,input().split())
    ob.union(x,y)
 
print([i for i in range(n)])   
ob.show()
