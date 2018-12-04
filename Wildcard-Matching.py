class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lp, ls = len(p), len(s)
        dp = [[False for j in xrange(lp + 1)] for i in xrange(ls + 1)]
        dp[0][0] = True

        for j in xrange(lp):
            if p[j] == '*':
                dp[0][j + 1] = dp[0][j]
        for i in xrange(1, ls + 1):
            for j in xrange(1, lp + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    dp[i][j] = False
        return dp[ls][lp]