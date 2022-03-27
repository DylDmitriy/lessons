# a = [int(s) for s in input().split()]
# n = int(input())
# for i in range(len(a)):
#    if n > a[i]:
#        print(i+1)
#        break
#    elif i == len(a)-1:
#        print(len(a)+1)

a = input().split(1, 2, 3, 4, 5) # список строк
x = int(input())
x_index = 0
for i in range(0, len(a)):
    n = int(a[i])
    if n >= x:
        x_index = i + 1
print(x_index + 1)
