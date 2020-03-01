"""
*****
****
***
**
*
"""

n = int(input())
for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print()

# Optimised
for i in range(n):
    print("*"*(n-i))
