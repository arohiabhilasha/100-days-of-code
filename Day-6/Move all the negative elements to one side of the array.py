def rearrange(arr, n):
    j=0
    for i in range(n):
        if arr[i]<0:
            arr[i], arr[j] = arr[j], arr[i]
            j+=1
    return arr
    
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
print(rearrange(arr, n))

#Time complexity= O(n)
#Space complexity= O(1)
