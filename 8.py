"""
1
2 3
4 5 6
7 8 9 10
"""

n = int(input())

for i in range(n):
    for j in range(i+1):
        print(i*(i+1)//2+1+j, end=" ")
    print()
