# A program to control the movement of a single motor using the RTK MCB!
# Composed by The Raspberry Pi Guy to accompany his tutorial!

import time
import RPi.GPIO as GPIO


def setuppins():
    # Next we setup the pins for use!
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(12,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(1,GPIO.OUT)
    GPIO.setup(5,GPIO.OUT)
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(22,GPIO.OUT)
    GPIO.setup(23,GPIO.OUT)


def motor1test():

    # Makes the motor spin one way for 3 seconds
    print("test forward")
    GPIO.output(12, True)
    GPIO.output(13, False)
    time.sleep(3)
    # Spins the other way for a further 3 seconds
    print("test backward")
    GPIO.output(12, False)
    GPIO.output(13, True)
    time.sleep(3)

    print('Finishing up!')
    GPIO.output(12, False)
    GPIO.output(13, False)
    
    return None


def motor2test():

    # Makes the motor spin one way for 3 seconds
    print("test forward")
    GPIO.output(1, True)
    GPIO.output(5, False)
    time.sleep(3)
    # Spins the other way for a further 3 seconds
    print("test backward")
    GPIO.output(1, False)
    GPIO.output(5, True)
    time.sleep(3)

    print('Finishing up!')
    GPIO.output(1, False)
    GPIO.output(5, False)
    
    return None

def motor3test():

    # Makes the motor spin one way for 3 seconds
    print("test forward")
    GPIO.output(17, True)
    GPIO.output(18, False)
    time.sleep(3)
    # Spins the other way for a further 3 seconds
    print("test backward")
    GPIO.output(17, False)
    GPIO.output(18, True)
    time.sleep(3)

    print('Finishing up!')
    GPIO.output(17, False)
    GPIO.output(18, False)
    
    return None

def motor4test():

    # Makes the motor spin one way for 3 seconds
    print("test forward")
    GPIO.output(22, True)
    GPIO.output(23, False)
    time.sleep(3)
    # Spins the other way for a further 3 seconds
    print("test backward")
    GPIO.output(22, False)
    GPIO.output(23, True)
    time.sleep(3)

    print('Finishing up!')
    GPIO.output(22, False)
    GPIO.output(23, False)
    
    return None

#motor 3 pins = 17,18
#motor 4 pins = 22,23

setuppins()
motor1test()
motor2test()
motor3test()
motor4test()