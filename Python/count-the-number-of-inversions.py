# Time:  O(n + max(end) * max(cnt)) <= O(n^3)
# Space: O(n + max(cnt)) <= O(n^2)

# dp, combinatorics, sliding window, two pointers
class Solution(object):
    def numberOfPermutations(self, n, requirements):
        """
        :type n: int
        :type requirements: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        lookup = [-1]*n
        for i, c in requirements:
            lookup[i] = c
        dp = [0]*(max(c for _, c in requirements)+1)
        dp[0] = 1
        for i in xrange(max(i for i, _ in requirements)+1):
            new_dp = [0]*len(dp)
            if lookup[i] != -1:  # optimized
                new_dp[lookup[i]] = reduce(lambda total, i: (total+dp[i])%MOD, xrange(max(lookup[i]-i, 0), lookup[i]+1), 0)
            else:            
                curr = 0
                for j in xrange(len(dp)):
                    curr += dp[j]
                    if j-(i+1) >= 0:
                        curr -= dp[j-(i+1)]
                    new_dp[j] = curr
            dp = new_dp
        return reduce(lambda total, i: total*(i+1)%MOD, xrange(i+1, n), reduce(lambda total, x: (total+x)%MOD, dp, 0))  # optimized


# Time:  O(n + max(end) * max(cnt)) <= O(n^3)
# Space: O(n + max(cnt)) <= O(n^2)
# dp, combinatorics, sliding window, two pointers
class Solution2(object):
    def numberOfPermutations(self, n, requirements):
        """
        :type n: int
        :type requirements: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        lookup = [-1]*n
        for i, c in requirements:
            lookup[i] = c
        dp = [0]*(max(c for _, c in requirements)+1)
        dp[0] = 1
        for i in xrange(n):
            new_dp = [0]*len(dp)
            curr = 0
            for j in xrange(len(dp)):
                curr += dp[j]
                if j-(i+1) >= 0:
                    curr -= dp[j-(i+1)]
                new_dp[j] = curr if lookup[i] == -1 or lookup[i] == j else 0
            dp = new_dp
        return reduce(lambda total, x: (total+x)%MOD, dp, 0)