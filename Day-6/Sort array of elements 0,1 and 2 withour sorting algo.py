class Solution:
    def sort012(self,arr,n):
        # code here
        c0=c1=c2=0
        for i in range(n):
            if arr[i] == 0:
                c0+=1
            elif arr[i] == 1:
                c1+=1
            else:
                c2+=1
        
        i=0
        while c0!=0:
            arr[i] = 0
            i+=1
            c0-=1
        while c1!=0:
            arr[i] = 1
            i+=1
            c1-=1
        while c2!=0:
            arr[i] = 2
            i+=1
            c2-=1
        return arr
      
#Time complexity = O(n) -------- 2 traversals
#Space complexity = O(1)

#Approach 2 with 1 traversal only
class Solution:
    def sort012(self,arr,n):
        # code here
        lo = mid =0
        hi = n-1
        while mid <= hi:
            if arr[mid] == 0:
                arr[lo], arr[mid] = arr[mid], arr[lo]
                lo+=1
                mid+=1
            elif arr[mid] == 1:
                mid+=1
            else:
                arr[mid], arr[hi] = arr[hi], arr[mid]
                hi-=1
                mid+=1
        
        return arr
