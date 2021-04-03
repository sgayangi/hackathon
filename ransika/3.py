# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for i in range(T):
    x,y=list(map(int,input().strip().split()))
    directions=input().strip()
    lookup={"U":0,"D":0,"L":0,"R":0}
    for i in directions:
        lookup[i]+=1
    x_=lookup["R"]-lookup["L"]
    y_=lookup["U"]-lookup["D"]
    #print(x_,y_)
    #print("before",lookup)
    if (x,y)==(x_,y_):
        print("YES")
    else:
        d_x,d_y=(x-x_),(y-y_)
        #print("delta",d_x,d_y)
        if d_x>=0:
            lookup["L"]-=d_x
        else:
            lookup["R"]+=d_x
        if d_y>=0:
            lookup["D"]-=d_y
        else:
            lookup["U"]+=d_y
        #print(lookup)
        if lookup["L"]>=0 and lookup["R"]>=0 and lookup["U"]>=0 and lookup["D"]>=0:
            print("YES")
        else:
            print("NO")