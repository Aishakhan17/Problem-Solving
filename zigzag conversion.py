import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result = [[] for _ in range(numRows)]
        current_row = 0
        direction = -1
        for char in s:
            result[current_row].append(char)

            if current_row == 0 or current_row == numRows - 1:
                direction = -direction

            current_row += direction

        return "".join("".join(row) for row in result)


solution = Solution()
s = "PAYPALISHIRING"
numRows = 3
print(solution.convert(s, numRows))
