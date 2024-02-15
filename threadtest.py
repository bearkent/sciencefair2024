import threading as t
from motorclass import Motor

pinlist = [12, 13, 1, 5, 17, 18, 22, 23]

m = Motor(pinlist)

m.setuppins()
t1 = t.Thread(target=m.motor1, args=[True, 1000])
t2 = t.Thread(target=m.motor2, args=[True, 1000])
t3 = t.Thread(target=m.motor3, args=[True, 1000])
t4 = t.Thread(target=m.motor4, args=[True, 1000])

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()



