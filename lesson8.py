text = input('Введите текст:')
result = {}
for key in text.split():
    if not result.get(key) == None:
        result[key] += 1
      else:
        result[key] = 1
for key, value in result.items():
    print(f'Слово: {key}, Количество: {value}')
