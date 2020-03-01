"""
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
"""

n = int(input())

for i in range(2*n):
    for j in range(2*n):
        if not i+j > n-1 or not (i-j)-n < 0 or not j-i < n or not i+j < 3*n - 1:
            print("*", end=" ")
        else:
            print(end="  ")
    print()
