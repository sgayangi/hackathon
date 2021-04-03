import array
from operator import add

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        h,m,H,M = list(map(int, input().split()))
        st_point = 60*h+m
        end_point = 60*H+M+5
        fin_point = 60*23+59
        comp_arr = array.array('I',[0,]*st_point)
        comp_arr.extend([1,]*(end_point-st_point))
        comp_arr.extend([0,]*(fin_point-end_point))
        if i== 0:
            add_arr = comp_arr
        else:
            add_arr = map(add, comp_arr, add_arr)
    print(max(add_arr))