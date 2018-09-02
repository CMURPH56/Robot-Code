import time 
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.IN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT) # Left Forward
GPIO.setup(18, GPIO.OUT) # Left Backward
GPIO.setup(20, GPIO.OUT) # Right Forward
GPIO.setup(26, GPIO.OUT) # Right Backward
speed  = 50
frequency = 50
fwd_right =  GPIO.PWM( 17, frequency)
bwd_right =  GPIO.PWM( 18, frequency)
fwd_left =  GPIO.PWM( 20, frequency)
bwd_left =  GPIO.PWM( 26, frequency)

def drive_forward():
    try:
        while True:
            fwd_right.start(speed)
            bwd_right.stop()
            fwd_left.start(speed)
            bwd_left.stop()
            sensor()
    except(KeyboardInterrupt):
        kill_power()


def reverse():

    try:
        while True:
            fwd_right.stop()
            bwd_right.start(speed)
            fwd_left.stop()
            bwd_left.start(speed)
            time.sleep(1)
            break
        turn_left()
    except(KeyboardInterrupt):
        kill_power()

def turn_left():
    print("turn left called")
    try:
        while True:
            fwd_left.start(speed)
            bwd_left.stop()
            time.sleep(0.5)
            break
        drive_forward()
     
    except(KeyboardInterrupt):
        kill_power()



def sensor():
    print("sensor called")
    i = GPIO.input(21)
    if i== 0:
        print("object detected")
        reverse()


def kill_power():
    print("killing power") 
    
    fwd_right.stop()
    bwd_right.stop()
    fwd_left.stop()
    bwd_left.stop()
    quit()


if __name__ == "__main__":
    drive_forward()
