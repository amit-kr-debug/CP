class Solution:
    # User function Template for python3

    # arr[]: Input Array
    # N : Size of the Array arr[]
    # Function to count inversions in the array
    def merge(self,arr,temp_arr,left,mid,right):
        i = left
        j = mid + 1
        k = left
        inv_count = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                k += 1
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += mid - i + 1
                k += 1
                j += 1

        while i <= mid:
            temp_arr[k] = arr[i]
            k += 1
            i += 1

        while j <= right:
            temp_arr[k] = arr[j]
            k += 1
            j+=1

        for i in range(left,right + 1):
            arr[i] = temp_arr[i]

        return inv_count

    def _mergeSort(self,arr,temp_arr,left,right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2

            inv_count += self._mergeSort(arr,temp_arr,left,mid)
            inv_count += self._mergeSort(arr,temp_arr,mid + 1,right)
            inv_count += self.merge(arr,temp_arr,left,mid,right)
        return inv_count

    def inversionCount(self,arr,n):
        # Your Code Here
        temp_arr = [0 for i in range(n)]
        return self._mergeSort(arr,temp_arr,0,n - 1)


ob = Solution()
print(ob.inversionCount([4,3,1,6,7,8], 6))