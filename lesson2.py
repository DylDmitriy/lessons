a = int (input("D:"))
a = ((a % 10)*100) + (((a // 10) % 10) * 10) + (a // 100)
print(a)
