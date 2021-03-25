# https://binarysearch.com/problems/Minimum-Initial-Value-for-Positive-Prefix-Sums
def min_val_prefix_sums(nums):
    nums.insert(0, 0)
    for i in range(1, len(nums)):
        nums[i] = nums[i-1] + nums[i]
    return 1 - min(nums)
