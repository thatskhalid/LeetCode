class Solution:
    def romanToInt(self, s: str) -> int:
        
        
        romannumbers = { 
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
        }
        
        #lets say s is III
        total = 0
        
        for x in range(len(s) - 1 ):
            current_numeral = romannumbers[s[x]]
            next_numeral = romannumbers[s[x+1]]
            
            if current_numeral < next_numeral:
                total -= current_numeral
            else: 
                total += current_numeral
                
        total += romannumbers[s[-1]]
        
        return total
    
solution = Solution()
solution.romanToInt
    