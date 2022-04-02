def checkio(number: int) -> int:
    number = str(number)
    x = 1
    for i in number:
        if i == '0':
            x *= 1
        else:
            x *= int(i)

    return x


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))
