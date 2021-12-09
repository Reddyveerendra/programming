n=list(map(int,input().split()))
N=len(n)-1
a=[]
while(N>=0):
    a.append(n[N])
    N-=1
print(a)