class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Store the max length of the non-repeating substring
        lens = 0
        # Save the characters of the current substring
        char = ""

        # Traverse the input
        for i in s:
            # Check if the current characters
            if i in char:
                # Remove characters if it's already in the substring
                index = char.index(i)
                char = char[index + 1:]
            # Add the current character
            char += i
            # Update the max length
            lens = max(lens, len(char))
        
        # Return the max length
        return lens