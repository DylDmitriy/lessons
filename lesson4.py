b = input("Введите высоту фигуры:")
size = int(b)
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1 # уменьшение m после каждого прохода цикла
    for j in range(0, i + 1):
        # вывод пирамиды из звёздочек
        print("*", end=' ')
    print(" ")
