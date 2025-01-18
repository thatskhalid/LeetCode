class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        
    #this dict is useless btw
        alphabet = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 
    'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 
    'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
        
        if not strs:
            return ""
        
        strs.sort()

        first_string = strs[0]
        last_string = strs[-1]
        
        common_prefix = ""
        for x in range(min(len(first_string), len(last_string))):
            if first_string[x] == last_string[x]:
                common_prefix += first_string[x]
            else:
                break
            
        return common_prefix

            
