"""
*****
 ****
  ***
   **
    *
"""

n = int(input())
for i in range(n):
    for j in range(n):
        if not i-j > 0:
            print("*", end="")
        else:
            print(end=" ")
    print()

# Optimised
for i in range(n):
    print(" "*i, end="")
    print("*"*(n-i))
