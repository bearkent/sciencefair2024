# A program to control the movement of a single motor using the RTK MCB!
# Composed by The Raspberry Pi Guy to accompany his tutorial!

# Let's import the modules we will need!
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


def motor1test():

    setuppins()

    # Makes the motor spin one way for 3 seconds
    print("test forward")
    GPIO.output(32, True)
    GPIO.output(33, False)
    time.sleep(3)
    # Spins the other way for a further 3 seconds
    print("test backward")
    GPIO.output(32, False)
    GPIO.output(33, True)
    time.sleep(3)

    print('Finishing up!')
    GPIO.output(32, False)
    GPIO.output(33, False)
    
    return None


def motor2test():

    setuppins()

    # Makes the motor spin one way for 3 seconds
    print("test forward")
    GPIO.output(28, True)
    GPIO.output(29, False)
    time.sleep(3)
    # Spins the other way for a further 3 seconds
    print("test backward")
    GPIO.output(28, False)
    GPIO.output(29, True)
    time.sleep(3)

    print('Finishing up!')
    GPIO.output(28, False)
    GPIO.output(29, False)
    
    return None


motor1test()
motor2test()