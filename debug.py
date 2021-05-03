class Solution:
    def sb(self,a,n,x):
        # Your code goes here
        currSum = 0
        minL = n + 1

        start = 0
        end = 0

        while end < n:
            while currSum <= x and end < n:
                currSum += a[end]
                end += 1
            while start < n and currSum > x:
                minL = min(minL,end - start)
                currSum -= a[start]
                start += 1

        return minL

ob = Solution()
print(ob.sb([1, 4, 45, 6, 0, 19],6,51))