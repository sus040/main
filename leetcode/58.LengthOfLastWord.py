class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # split string based on comma
        letters = s.split()
        if not letters:
          return 0
        return len(letters[-1])
