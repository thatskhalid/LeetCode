class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        
        i, length = len(s) - 1, 0 #length is the length of s and we're starting at -1, and it's initially 0
        
        while s[i] == " ":
            i -= 1
            
            #i think here we're just deleting the leading whitespace
        
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
            
        return length