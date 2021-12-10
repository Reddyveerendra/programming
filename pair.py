k=int(input("difference:\t"))
n=list(map(int,input("enter elements:\t").split()))
for i in range(0,len(n)):
    a=n[i]
    for j in range(0,len(n)):
        b=n[j]
        if((k==a-b) and i!=j):
            print((a,b))