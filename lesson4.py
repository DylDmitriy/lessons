a = 123
if a == 123:
    print(321)
else:
    print(none)

def reverse_number(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n /= 10
    return r









 result= reverse_number(123)
print(result)