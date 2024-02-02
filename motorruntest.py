from motor import Motor
import utime

# GPIO Pin
MOTOR1_PIN_1 = 32
MOTOR1_PIN_2 = 33
MOTOR2_PIN_1 = None
MOTOR2_PIN_2 = None
MOTOR3_PIN_1 = None
MOTOR3_PIN_2 = None
MOTOR4_PIN_1 = None
MOTOR4_PIN_2 = None



motor_pins = [MOTOR1_PIN_1, MOTOR1_PIN_2, MOTOR2_PIN_1, MOTOR2_PIN_2, MOTOR3_PIN_1, MOTOR3_PIN_2, MOTOR4_PIN_1, MOTOR4_PIN_2]

# Create an instance of motor
motor = Motor(motor_pins, 20000)



if __name__ == '__main__':
    try:
        # Test forward, reverse, stop
        print("*********Testing motor 1 forward, backward*********")
        for i in range(2):
            motor.motor1_f()
            print("running forward")
            utime.sleep(2)

            motor.stop()
            utime.sleep(2)

            motor.motor1_b()
            print("running backward")
            utime.sleep(2)

            motor.stop()
            
        print("*********Testing speed*********")
        for i in range(2):
            print("Moving at 100% speed")
            motor.change_speed(100);
            motor.motor1_f()
            utime.sleep(2)
            
            print("Moving at 50% speed")
            motor.change_speed(50);
            motor.motor1_f()
            utime.sleep(2)
            
            print("Moving at 20% of speed")
            motor.change_speed(20);
            motor.motor1_f()
            utime.sleep(2)
            
            print("Moving at 0% of speed or the slowest")
            motor.change_speed(0);
            motor.motor1_f()
            utime.sleep(2)
            
        motor.deinit()

    except KeyboardInterrupt:
        motor.deinit()