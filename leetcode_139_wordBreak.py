class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = dict()
        return self.wordBreakAux(s, wordDict, 0, memo)
    
    def wordBreakAux(self, s, wordDict, idx, memo):
        if s=="":
            return True
        for word in wordDict:
            if len(s)<len(word):
                continue
            s_left = s[:len(word)]
            s_right = s[len(word):]
            
            if s_left == word:
                next_idx = idx+len(word)
                if next_idx not in memo:
                    memo[next_idx] = self.wordBreakAux(s_right, wordDict, next_idx, memo)
                if memo[next_idx]:
                    return True
        return False
