"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


class Solution:
    def threeSum(self,nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        i = 0
        while i < n - 2:
            a = nums[i]
            low = i + 1
            high = n - 1
            while low < high:
                sumz = a + nums[low] + nums[high]
                if sumz == 0:
                    temp = [a,nums[low],nums[high]]
                    ans.append(temp)
                    prevlow = nums[low]
                    prevhigh = nums[high]
                    while low < n and nums[low] == prevlow:
                        low += 1
                    while high > 0 and nums[high] == prevhigh:
                        high -= 1

                elif sumz < 0:
                    low += 1
                else:
                    high -= 1
            while i < n and a == nums[i]:
                i += 1

        return ans

