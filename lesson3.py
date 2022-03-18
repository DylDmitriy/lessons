a = "This is my {} book".format("new")
print(a)
a = "This is my {} book".format("замена в строке")
print(a)
a = "This is my замена в строке book"
if a.count("строке"):
    print("Да")
else:
    print("Нет")


