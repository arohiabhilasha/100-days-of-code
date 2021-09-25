#Approach 1 - Time complexity- O(n logn)
class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        if k<=r+1:
            arr.sort()
            return arr[k-1]
          
#Approach 2- Priority queue, Time complexity-          
import heapq
class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        heapq.heapify(arr)
        for i in range(k):
            res = heapq.heappop(arr)
        return res
            
       
#C++
#Approach 2- Priority queue, Time complexity- 
class Solution{
    public:
    // arr : given array
    // l : starting index of the array i.e 0
    // r : ending index of the array i.e size-1
    // k : find kth smallest element and return using this function
    int kthSmallest(int arr[], int l, int r, int k) {
        //code here
        priority_queue<int> maxHeap;
        for(int i=l;i<=r;i++){
            maxHeap.push(arr[i]);
            if(maxHeap.size() > k){
                maxHeap.pop();
        }
        return maxHeap.top();
    }
};
