# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = {}
        length = 0
        l = 0
        for i in range(len(s)):
            if s[i] in substr.keys() and substr[s[i]] >= l:
                length = max(length,i-l)
                l = substr[s[i]] + 1
                substr[s[i]] = i
            else:
                substr[s[i]] = i
        length = max(length,len(s)-l)
        return length