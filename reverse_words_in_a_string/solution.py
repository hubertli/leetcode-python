"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

"""

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        tmp = s.split()
        tmp.reverse()
        tmp = ' '.join(tmp)
        return (tmp)

s = Solution()
print(s.reverseWords("the sky is blue"))
