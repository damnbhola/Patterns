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

# Optimized
for i in range(n):
    print(""*i, end="")
    print("*"*(n-i))
