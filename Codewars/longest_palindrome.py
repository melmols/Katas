class Solution(object):
    # Define palindrome.
    def palindrome(self, s):
        return s == s[::-1]

    def substrings(self, s):
        l = len(s)

        for end in range(l, 0, -1):
            for i in range(l - end + 1):
                yield s[i: i + end]

    # main function
    def longestPalindrome(self, s):
        for l in self.substrings(s):
            if self.palindrome(l):
                return l