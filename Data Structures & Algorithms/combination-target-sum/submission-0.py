class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        output = []

        def search(start, remaining, combination):
            # We have found a combination that adds up to target
            if remaining == 0:
                output.append(combination)
                return

            # Only consider this number and the numbers after it
            for i in range(start, len(nums)):
                number = nums[i]

                # A number larger than what remains cannot help
                if number > remaining:
                    continue

                # Use i again because the same number is allowed repeatedly
                search(i, remaining - number, combination + [number])

        search(0, target, [])
        return output
        