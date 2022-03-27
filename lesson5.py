a = [int(s) for s in input().split()]
n = int(input())
for i in range(len(a)):
    if n > a[i]:
        print(i+1)
        break
    elif i == len(a)-1:
        print(len(a)+1)
