x = int(input("Введите первое число : "))
y = int(input("Введите второе чиcло : "))
z = input("Введите знак (+, -, *, / ) : ")
def arithmetic (x, y, z):
	if z == "+" :
		return (x + y)
	elif z == "-":
		return (x - y)
	elif z == "*":
		return (x * y)
	elif z == "/":
		return (x / y)
	else :
		return ("Invalid operation")
print (arithmetic(x, y, z))

