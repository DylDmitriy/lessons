password = input()
repassword = input()
a = 0
while a == 0:
    if len(password) < 5:
        print("Короткий!")
        password = input()
        repassword = input()
    elif "123" in password:
        print("Простой!")
        password = input()
        repassword = input()
    elif password != repassword:
        print("Различаются.")
        password = input()
        repassword = input()                
    else:
        print("OK")
        a += 2
