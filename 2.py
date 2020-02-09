"""
    *
   **
  ***
 ****
*****
"""

n = int(input())
for i in range(n):
    for j in range(n):
        if i+j >= n-1:
            print("*", end="")
        else:
            print(end=" ")
    print()

# Optimised
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"*i)
