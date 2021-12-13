n=list(map(int,input().split()))
a=n[0]
for i in range(1,int(len(n))):
    if(a>n[i]):
        a=n[i]
    else:
        continueCHE
print(a)