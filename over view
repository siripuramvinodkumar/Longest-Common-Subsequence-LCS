# Longest-Common-Subsequence-LCS
This repository contains a Python implementation of the Longest Common Subsequence (LCS) algorithm. It provides a solution to find the length of the longest subsequence common to two given strings.

Files:

-   `lcs.py`: Contains the Python implementation of the LCS algorithm.
-   `README.md`: Provides information about the repository, usage instructions, and examples.
-   `test_cases.txt`: contains test cases for running the code.

lcs.py:

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

test_cases.txt:

Plaintext

3
ABCDGH
AEDFHR
ABC
AC
XYZW
XYWZ

README.md:

Markdown

# Longest Common Subsequence (LCS)

This repository contains a Python implementation of the Longest Common Subsequence (LCS) algorithm.

## Description

The Longest Common Subsequence (LCS) problem involves finding the longest subsequence common to two given strings. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

## Usage

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2.  Navigate to the repository directory:

    ```bash
    cd Longest-Common-Subsequence-LCS
    ```

3.  Run the `lcs.py` script:

    ```bash
    python lcs.py
    ```
    the lcs.py file automatically reads test cases from test_cases.txt.

## Example

Input Strings:

-   `s1 = "ABCDGH"`
-   `s2 = "AEDFHR"`

Output:

3


Explanation: The longest common subsequence is "ADH", which has a length of 3.

## Complexity

-   Time Complexity: O(n * m), where n and m are the lengths of the input strings.
-   Space Complexity: O(n * m)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements
