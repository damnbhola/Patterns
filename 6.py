"""
        *
      *   *
    *       *
  *           *
*               *
  *           *
    *       *
      *   *
        *
"""

n = int(input())

for i in range(2*n-1):
    for j in range(2*n-1):
        if i+j == n-1 or (i-j)-n+1 == 0 or j-i == n-1 or i+j == 3*n - 3:
            print("*", end=" ")
        else:
            print(end="  ")
    print("")
