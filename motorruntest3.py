from motorclass import Motor
import time

pinlist = [12, 13, 1, 5, 17, 18, 22, 23]

motor = Motor(pinlist)

time.sleep(5)

motor.setuppins()
motor.motor1(True,500)
motor.motor2(True,500)
motor.motor3(True,500)
motor.motor4(True,500)