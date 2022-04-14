from datetime import datetime, timedelta
import time


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



beg = datetime.strptime(str('00:05:00'), '%H:%M:%S')
end = datetime.strptime(str('00:00:00'), '%H:%M:%S')
step = timedelta(seconds=1)
while beg != end:
    beg = beg - step
    print(str(beg).split()[1])
    time.sleep(1)
