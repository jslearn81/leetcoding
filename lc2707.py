class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
 
        sub_char = set()
        for w in dictionary:
            for i in range(len(w)+1):
                sub_char.add(w[:i])
        
        @cache
        def dp(i):
            if i>=len(s):
                return 0
            
            res = 1 + dp(i+1)
            for j in range(i,len(s)):
                if s[i:(j+1)] not in sub_char:
                    return min(res,j-i+1+dp(j+1))
                if s[i:(j+1)] in dictionary:
                    res = min(res,dp(j+1))
            
            return res

        return dp(0)
