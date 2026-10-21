class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = 0
        left = len(heights) - 1
        maxi = 0

        while right < left:
            area = (left - right) * min(heights[left], heights[right])
            maxi = max(maxi, area)

            if heights[left] < heights[right]:
                left -= 1
            else:
                right += 1

        return maxi
                    