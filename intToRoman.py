class Solution:
    def intToRoman(self, num: int) -> str:
        symbolDict = {
            1: {1: "I", 10: "X", 100: "C", 1000: "M"},
            2: {2: "II", 20: "XX", 200: "CC", 2000: "MM"},
            3: {3: "III", 30: "XXX", 300: "CCC", 3000: "MMM"},
            4: {4: "IV", 40: "XL", 400: "CD"},
            5: {5: "V", 50: "L", 500: "D"},
            6: {6: "VI", 60: "LX", 600: "DC"},
            7: {7: "VII", 70: "LXX", 700: "DCC"},
            8: {8: "VIII", 80: "LXXX", 800: "DCCC"},
            9: {9: "IX", 90: "XC", 900: "CM"},
        }
        result = []

        div = 10
        i = 1
        while num != 0:
            curr = num % div
            num = num // div
            if curr != 0:
                result.append(symbolDict[curr][curr * i])
            i *= 10
        return "".join(result[::-1])


solution = Solution()
print(solution.intToRoman(10))
