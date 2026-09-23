class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        numbers = sorted(nums)
        result: List[List[int]] = []

        for i in range(len(numbers)):
            # skip duplicates
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            
            # two pointers
            left = i + 1
            right = len(numbers) - 1
            #  dynamically iterate over the 2 pointers
            while left < right:
                curr_sum = numbers[i] + numbers[left] + numbers[right]

                if curr_sum == 0:
                    result.append([numbers[i],numbers[left],numbers[right]])
                    left += 1
                    right -= 1
                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1

                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1

                elif curr_sum < 0:
                    left += 1
            
                else :
                    right -= 1

        return result
        