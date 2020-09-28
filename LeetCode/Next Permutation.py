"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution :
    def nextPermutation(self, nums) -> None :
        """
        Do not return anything, modify nums in-place instead.
        """
        print(nums)
        index = len(nums) - 1
        fSwap = -1
        sSwap = -1
        minD = 10000000000
        flag = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                flag = -1
                break
        if flag == 1:
            nums.sort()
            return nums
        for i in range(1, len(nums) - 1) :
            if nums[i + 1] <= nums[i] > nums[i - 1]:
                index = i

        if nums[len(nums) - 1] > nums[len(nums) - 2]:
            index = len(nums) - 1
        print("index", index)
        for i in range(index + 1, len(nums)) :
            if nums[i] > nums[index] and nums[i] - nums[index] < minD :
                fSwap = i
        print("fs", fSwap)
        if fSwap == -1:
            for i in range(index, len(nums)):
                if nums[i] > nums[index - 1] and nums[i] - nums[index - 1] < minD :
                    sSwap = i
            print("ss", sSwap)
            nums[sSwap], nums[index - 1] = nums[index - 1], nums[sSwap]
            nums[index:] = sorted(nums[index:])
            return nums
        else:
            nums[fSwap], nums[index] = nums[index], nums[fSwap]
            if index + 1 != len(nums):
                nums[index+1:] = sorted(nums[index+1:])
            return nums

ob = Solution()

print(ob.nextPermutation([4,2,4,4,3]))