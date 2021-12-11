def getMissingNum(a, n):
    new=n*(n+1)//2
    return new-sum(a)
if __name__=='__main__':
    a = list(map(int,input().split()))
    n = len(a)+1
    miss_number = getMissingNum(a, n)
    print(miss_number)