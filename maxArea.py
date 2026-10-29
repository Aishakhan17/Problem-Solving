import math


class Solution:
    def maxArea(self, height: list[int]) -> int:
        if len(height) <= 1:
            return 0

        max_quantity = -math.inf
        i = 0
        j = len(height) - 1

        while i < j:
            left_line = height[i]
            right_line = height[j]
            max_quantity = max(max_quantity, (j - i) * min(left_line, right_line))

            if left_line > right_line:
                j -= 1
            else:
                i += 1
        return max_quantity
