```python
class Solution:
    def lcs(self, s1, s2):
        n = len(s1)
        m = len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]

if __name__ == '__main__':
    with open('test_cases.txt', 'r') as f:
        lines = f.readlines()
        test_cases = int(lines[0].strip())
        line_index = 1
        for _ in range(test_cases):
            s1 = lines[line_index].strip()
            line_index+=1
            s2 = lines[line_index].strip()
            line_index+=1
            ob = Solution()
            print(ob.lcs(s1, s2))
