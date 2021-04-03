t=int(input())
for i in range(t):
    N,M=list(map(int,input().strip().split()))
    lis=list(map(int,input().strip().split()))
    check={}
    for i in range(0,N):
        check[lis[i]]="True"
    for j in range(N,N+M):
        try:
            a=check[lis[j]]
            print("YES")
        except:
            print("NO")
            check[lis[j]]="True"