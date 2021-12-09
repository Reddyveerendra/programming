n = list(map(int,input("enter elements of array\t").split()))
N = int(input("enter element to find\t"))
for i in range(0,len(n)):
    if (n[i]==N):
        print(i)
else:
    print("element not in list")