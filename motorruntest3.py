from motorclass import Motor
import time

pinlist = [12, 13, 1, 5, 17, 18, 22, 23]

motor = Motor(pinlist)

time.sleep(5)

motor.setuppins()
motor.motor1(True,1000)
motor.motor2(True,1000)
motor.motor3(True,1000)
motor.motor4(True,1000)