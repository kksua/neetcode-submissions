class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        sorted_nums = sorted(nums)
        count = 1
        longest = 1

        for n in range(len(sorted_nums) - 1):
            if sorted_nums[n] == sorted_nums[n + 1]:
                continue  

            if sorted_nums[n] + 1 == sorted_nums[n + 1]:
                count += 1
            else:
                count = 1  

            longest = max(longest, count)

        return longest


        