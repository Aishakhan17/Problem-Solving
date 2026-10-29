class Solution:
    def longestPalindrome(self, s: str) -> str:
        # longest would the string itself - check if that's the case
        is_palindrome = self.check_palindrome(s)
        if is_palindrome:
            return s
        longest_palindrome = ""
        i = 0
        j = i + 1
        while i < len(s):
            string = s[i:j]
            is_palindrome = self.check_palindrome(string)
            if is_palindrome:
                if len(string) > len(longest_palindrome):
                    longest_palindrome = string
            j += 1
            if j > len(s):
                i += 1
                j = i + 1
        return longest_palindrome

    def check_palindrome(self, string):
        if len(string) <= 1:
            first = second = string
        else:
            mid_point = int(len(string) // 2)
            if len(string) % 2 == 0:
                first, second = string[:mid_point], string[mid_point:]
            else:
                first, second = string[:mid_point], string[mid_point + 1 :]
        return first == second[::-1]
