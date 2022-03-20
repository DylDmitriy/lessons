b = input("Введите что-нибудь:")
a = "Это строка в которую {} новую строку".format(b)
print(a)
с = a.replace(b, "замена в строке")
print(с)
print(len(с))
if с.count("строке"):
    print("Да")
else:
    print("Нет")


