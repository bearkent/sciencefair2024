# A program to control the movement of a single motor using the RTK MCB!
# Composed by The Raspberry Pi Guy to accompany his tutorial!

# Let's import the modules we will need!
import time
import RPi.GPIO as GPIO

# Next we setup the pins for use!
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)

print('Starting motor sequence!')


    # Makes the motor spin one way for 3 seconds
print("test forward")
GPIO.output(32, True)
GPIO.output(33, False)
time.sleep(30)
    # Spins the other way for a further 3 seconds
print("test backward")
GPIO.output(32, False)
GPIO.output(33, True)
time.sleep(3)
    # If a keyboard interrupt is detected then it exits cleanly!
print('Finishing up!')
GPIO.output(32, False)
GPIO.output(33, False)
quit()