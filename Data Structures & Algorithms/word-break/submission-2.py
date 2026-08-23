class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        # Default case
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if len(word) > len(s) - i:
                    continue
                if word == s[i:i+len(word)]:
                    dp[i] = True and dp[i+len(word)]
                if dp[i]:
                    break
        return dp[0]


        