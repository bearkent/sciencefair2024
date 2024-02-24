import time
import RPi.GPIO as GPIO

class Motor:

    def __init__(self, pinlist:list) -> None:

        self.pinlist = pinlist

        # pinlist[0] = self.pinlist[0]  #motor1 pin1
        # pinlist[1] = self.pinlist[1]
        # pinlist[2] = self.pinlist[2]
        # pinlist[3] = self.pinlist[3]
        # pinlist[4] = self.pinlist[4]
        # pinlist[5] = self.pinlist[5]
        # pinlist[6] = self.pinlist[6]
        # pinlist[7] = self.pinlist[7]

        

    def setuppins(self):
    # Next we setup the pins for use!
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pinlist[0],GPIO.OUT)
        GPIO.setup(self.pinlist[1],GPIO.OUT)
        GPIO.setup(self.pinlist[2],GPIO.OUT)
        GPIO.setup(self.pinlist[3],GPIO.OUT)
        GPIO.setup(self.pinlist[4],GPIO.OUT)
        GPIO.setup(self.pinlist[5],GPIO.OUT)
        GPIO.setup(self.pinlist[6],GPIO.OUT)
        GPIO.setup(self.pinlist[7],GPIO.OUT)

    def motor4(self, k:bool, t:int):
        if k:
            print(f"motor 4 forward for {t} milliseconds")
            GPIO.output(self.pinlist[0], True)
            GPIO.output(self.pinlist[1], False)
            time.sleep(t/1000)
        else:
            print(f"motor 4 backward for {t} milliseconds")
            GPIO.output(self.pinlist[0], False)
            GPIO.output(self.pinlist[1], True)
            time.sleep(t/1000)

        GPIO.output(self.pinlist[0], False)
        GPIO.output(self.pinlist[1], False)

    def motor3(self, k:bool, t:int):
        if k:
            print(f"motor 3 forward for {t} milliseconds")
            GPIO.output(self.pinlist[2], True)
            GPIO.output(self.pinlist[3], False)
            time.sleep(t/1000)
        else:
            print(f"motor 3 backward for {t} milliseconds")
            GPIO.output(self.pinlist[2], False)
            GPIO.output(self.pinlist[3], True)
            time.sleep(t/1000)

        GPIO.output(self.pinlist[2], False)
        GPIO.output(self.pinlist[3], False)

    def motor2(self, k:bool, t:int):
        if k:
            print(f"motor 2 forward for {t} milliseconds")
            GPIO.output(self.pinlist[4], True)
            GPIO.output(self.pinlist[5], False)
            time.sleep(t/1000)
        else:
            print(f"motor 2 backward for {t} milliseconds")
            GPIO.output(self.pinlist[4], False)
            GPIO.output(self.pinlist[5], True)
            time.sleep(t/1000)

        GPIO.output(self.pinlist[4], False)
        GPIO.output(self.pinlist[5], False)

    def motor1(self, k:bool, t:int):
        if k:
            print(f"motor 1 forward for {t} milliseconds")
            GPIO.output(self.pinlist[6], True)
            GPIO.output(self.pinlist[7], False)
            time.sleep(t/1000)
        else:
            print(f"motor 1 backward for {t} milliseconds")
            GPIO.output(self.pinlist[6], False)
            GPIO.output(self.pinlist[7], True)
            time.sleep(t/1000)

        GPIO.output(self.pinlist[6], False)
        GPIO.output(self.pinlist[7], False)

