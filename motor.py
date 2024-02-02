from machine import Pin
from machine import PWM
import utime

'''
Class to represent our motor
'''
class Motor:
    MAX_DUTY_CYCLE = 65535
    MIN_DUTY_CYCLE = 0
    def __init__(self, motor_pins, frequency=20000):
        self.motor1_pin1 = PWM(Pin(motor_pins[0], mode=Pin.OUT))
        self.motor1_pin2 = PWM(Pin(motor_pins[1], mode=Pin.OUT))
        self.motor2_pin1 = PWM(Pin(motor_pins[2], mode=Pin.OUT))
        self.motor2_pin2 = PWM(Pin(motor_pins[3], mode=Pin.OUT))
        self.motor3_pin1 = PWM(Pin(motor_pins[4], mode=Pin.OUT))
        self.motor3_pin2 = PWM(Pin(motor_pins[5], mode=Pin.OUT))
        self.motor4_pin1 = PWM(Pin(motor_pins[6], mode=Pin.OUT))
        self.motor4_pin2 = PWM(Pin(motor_pins[7], mode=Pin.OUT))

        # set PWM frequency

        self.motor1_pin1.freq(frequency)
        self.motor1_pin2.freq(frequency)
        self.motor2_pin1.freq(frequency)
        self.motor2_pin2.freq(frequency)
        self.motor3_pin1.freq(frequency)
        self.motor3_pin2.freq(frequency)
        self.motor4_pin1.freq(frequency)
        self.motor4_pin2.freq(frequency)

        
        self.current_speed = Motor.MAX_DUTY_CYCLE

    def motor1_f(self):
        self.motor1_pin1.duty_u16(self.current_speed)
        self.motor1_pin2.duty_u16(Motor.MIN_DUTY_CYCLE)

    def motor1_b(self):
        self.motor1_pin1.duty_u16(Motor.MIN_DUTY_CYCLE)
        self.motor1_pin2.duty_u16(self.current_speed)


    def motor2_f(self):
        self.motor2_pin1.duty_u16(self.current_speed)
        self.motor2_pin2.duty_u16(Motor.MIN_DUTY_CYCLE)

    def motor2_b(self):
        self.motor2_pin1.duty_u16(Motor.MIN_DUTY_CYCLE)
        self.motor2_pin2.duty_u16(self.current_speed)


    def motor3_f(self):
        self.motor3_pin1.duty_u16(self.current_speed)
        self.motor3_pin2.duty_u16(Motor.MIN_DUTY_CYCLE)

    def motor3_b(self):
        self.motor3_pin1.duty_u16(Motor.MIN_DUTY_CYCLE)
        self.motor3_pin2.duty_u16(self.current_speed)

    
    def motor4_f(self):
        self.motor4_pin1.duty_u16(self.current_speed)
        self.motor3_pin2.duty_u16(Motor.MIN_DUTY_CYCLE)

    def motor4_b(self):
        self.motor3_pin1.duty_u16(Motor.MIN_DUTY_CYCLE)
        self.motor3_pin2.duty_u16(self.current_speed)
        
    # def move_forward(self):
    #     self.motor1_pin1.duty_u16(self.current_speed)
    #     self.motor1_pin2.duty_u16(Motor.MIN_DUTY_CYCLE)
        
    #     self.motor2_pin1.duty_u16(self.current_speed)
    #     self.motor2_pin2.duty_u16(Motor.MIN_DUTY_CYCLE)
           
    # def move_backward(self):
    #     self.motor1_pin1.duty_u16(Motor.MIN_DUTY_CYCLE)
    #     self.motor1_pin2.duty_u16(self.current_speed)
        
    #     self.motor2_pin1.duty_u16(Motor.MIN_DUTY_CYCLE)
    #     self.motor2_pin2.duty_u16(self.current_speed)
        
    # def turn_left(self):
    #     self.motor1_pin1.duty_u16(self.current_speed)
    #     self.motor1_pin2.duty_u16(Motor.MIN_DUTY_CYCLE)
        
    #     self.motor2_pin1.duty_u16(Motor.MAX_DUTY_CYCLE)
    #     self.motor2_pin2.duty_u16(Motor.MAX_DUTY_CYCLE)
        
    # def turn_right(self):
    #     self.motor1_pin1.duty_u16(Motor.MAX_DUTY_CYCLE)
    #     self.motor1_pin2.duty_u16(Motor.MAX_DUTY_CYCLE)
        
    #     self.motor2_pin1.duty_u16(self.current_speed)
    #     self.motor2_pin2.duty_u16(Motor.MIN_DUTY_CYCLE)
        
    def stop(self):
        self.motor1_pin1.duty_u16(Motor.MIN_DUTY_CYCLE)
        self.motor1_pin2.duty_u16(Motor.MIN_DUTY_CYCLE)
        
        self.motor2_pin1.duty_u16(Motor.MIN_DUTY_CYCLE)
        self.motor2_pin2.duty_u16(Motor.MIN_DUTY_CYCLE)

        self.motor3_pin1.duty_u16(Motor.MIN_DUTY_CYCLE)
        self.motor3_pin2.duty_u16(Motor.MIN_DUTY_CYCLE)

        self.motor4_pin1.duty_u16(Motor.MIN_DUTY_CYCLE)
        self.motor4_pin2.duty_u16(Motor.MIN_DUTY_CYCLE)
        
    ''' Map duty cycle values from 0-100 to duty cycle 40000-65535 '''
    def __map_range(self, x, in_min, in_max, out_min, out_max):
      return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
        
    ''' new_speed is a value from 0% - 100% '''
    def change_speed(self, new_speed):
        new_duty_cycle = self.__map_range(new_speed, 0, 100, 40000, 65535)
        self.current_speed = new_duty_cycle

        
    def deinit(self):
        """deinit PWM Pins"""
        print("Deinitializing PWM Pins")
        self.stop()
        utime.sleep(0.1)
        self.motor1_pin1.deinit()
        self.motor1_pin2.deinit()
        self.motor2_pin1.deinit()
        self.motor2_pin2.deinit()
        self.motor3_pin1.deinit()
        self.motor3_pin2.deinit()
        self.motor4_pin1.deinit()
        self.motor4_pin2.deinit()