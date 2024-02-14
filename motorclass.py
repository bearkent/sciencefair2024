import time
import RPi.GPIO as GPIO

class Motor:

    def __init__(self, pinlist:list) -> None:

        self.pinlist[0] = m1pin1
        self.pinlist[1] = m1pin2
        self.pinlist[2] = m2pin1
        self.pinlist[3] = m2pin2
        self.pinlist[4] = m3pin1
        self.pinlist[5] = m3pin2
        self.pinlist[6] = m4pin1
        self.pinlist[7] = m4pin2

        

    def setuppins(self):
    # Next we setup the pins for use!
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(m1pin1,GPIO.OUT)
        GPIO.setup(m1pin2,GPIO.OUT)
        GPIO.setup(m2pin1,GPIO.OUT)
        GPIO.setup(m2pin2,GPIO.OUT)
        GPIO.setup(m3pin1,GPIO.OUT)
        GPIO.setup(m3pin2,GPIO.OUT)
        GPIO.setup(m4pin1,GPIO.OUT)
        GPIO.setup(m4pin2,GPIO.OUT)

    def motor1(self, k:bool, t:int):
        if k:
            print(f"motor 1 forward for {t} milliseconds")
            GPIO.output(m1pin1, True)
            GPIO.output(m1pin2, False)
            time.sleep(t/1000)
        else:
            print(f"motor 1 backward for {t} milliseconds")
            GPIO.output(m1pin1, False)
            GPIO.output(m1pin2, True)
            time.sleep(t/1000)

    def motor2(self, k:bool, t:int):
        if k:
            print(f"motor 2 forward for {t} milliseconds")
            GPIO.output(m2pin1, True)
            GPIO.output(m2pin2, False)
            time.sleep(t/1000)
        else:
            print(f"motor 2 backward for {t} milliseconds")
            GPIO.output(m2pin1, False)
            GPIO.output(m2pin2, True)
            time.sleep(t/1000)

    def motor3(self, k:bool, t:int):
        if k:
            print(f"motor 3 forward for {t} milliseconds")
            GPIO.output(m3pin1, True)
            GPIO.output(m3pin2, False)
            time.sleep(t/1000)
        else:
            print(f"motor 3 backward for {t} milliseconds")
            GPIO.output(m3pin1, False)
            GPIO.output(m3pin2, True)
            time.sleep(t/1000)

    def motor4(self, k:bool, t:int):
        if k:
            print(f"motor 4 forward for {t} milliseconds")
            GPIO.output(m4pin1, True)
            GPIO.output(m4pin2, False)
            time.sleep(t/1000)
        else:
            print(f"motor 4 backward for {t} milliseconds")
            GPIO.output(m4pin1, False)
            GPIO.output(m4pin2, True)
            time.sleep(t/1000)


# def motor1test():

#     # Makes the motor spin one way for 3 seconds
#     print("test forward")
#     GPIO.output(12, True)
#     GPIO.output(13, False)
#     time.sleep(3)
#     # Spins the other way for a further 3 seconds
#     print("test backward")
#     GPIO.output(12, False)
#     GPIO.output(13, True)
#     time.sleep(3)

#     print('Finishing up!')
#     GPIO.output(12, False)
#     GPIO.output(13, False)
    
#     return None


# def motor2test():

#     # Makes the motor spin one way for 3 seconds
#     print("test forward")
#     GPIO.output(1, True)
#     GPIO.output(5, False)
#     time.sleep(3)
#     # Spins the other way for a further 3 seconds
#     print("test backward")
#     GPIO.output(1, False)
#     GPIO.output(5, True)
#     time.sleep(3)

#     print('Finishing up!')
#     GPIO.output(1, False)
#     GPIO.output(5, False)
    
#     return None

# def motor3test():

#     # Makes the motor spin one way for 3 seconds
#     print("test forward")
#     GPIO.output(17, True)
#     GPIO.output(18, False)
#     time.sleep(3)
#     # Spins the other way for a further 3 seconds
#     print("test backward")
#     GPIO.output(17, False)
#     GPIO.output(18, True)
#     time.sleep(3)

#     print('Finishing up!')
#     GPIO.output(17, False)
#     GPIO.output(18, False)
    
#     return None

# def motor4test():

#     # Makes the motor spin one way for 3 seconds
#     print("test forward")
#     GPIO.output(22, True)
#     GPIO.output(23, False)
#     time.sleep(3)
#     # Spins the other way for a further 3 seconds
#     print("test backward")
#     GPIO.output(22, False)
#     GPIO.output(23, True)
#     time.sleep(3)

#     print('Finishing up!')
#     GPIO.output(22, False)
#     GPIO.output(23, False)
    
#     return None

# #motor 3 pins = 17,18
# #motor 4 pins = 22,23

# setuppins()
# motor1test()
# motor2test()
# motor3test()
# motor4test()