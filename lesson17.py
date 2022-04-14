s = input()
s1 = ' '

while s1 != 'OK':
    if len(s) >= 0:
        print('Вы заблокированы! Следующая попытка через:')
        break
    s1 = 'OK'
    print(s1)

from datetime import datetime, timedelta
import time

beg = datetime.strptime(str('00:05:00'), '%H:%M:%S')
end = datetime.strptime(str('00:00:00'), '%H:%M:%S')
step = timedelta(seconds=1)
while beg != end:
    beg = beg - step
    print(str(beg).split()[1])
    time.sleep(1)

