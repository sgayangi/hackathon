N=int(input())
lis=list(map(int,input().strip().split(" ")))
def bubbleSort(arr):
    n = len(arr)
    ct=0
    # go through all
    for i in range(n):
        swapped = False
  
        # Last i elements ready
        for j in range(0, n-i-1):
   
            # traverse
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                ct+=1
        # IF no two elements were swapped
        if swapped == False:
            break
    return ct
print(bubbleSort(lis))