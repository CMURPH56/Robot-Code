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



def drive_forward():
    try:
        while True:
            GPIO.output( 17, True)
            GPIO.output( 18, False)
            GPIO.output( 20, True)
            GPIO.output( 26, False)
            sensor()
    except(KeyboardInterrupt):
        kill_power()


def reverse():

    try:
        while True:
            GPIO.output( 17, False)
            GPIO.output( 18, True)
            GPIO.output( 20, False)
            GPIO.output( 26, True)
            time.sleep(1)
            break
        turn_left()
    except(KeyboardInterrupt):
        kill_power()

def turn_left():

    try:
        while True:
            GPIO.output( 20, True)
            GPIO.output( 26, False)
            time.sleep(0.5)
            break
        drive_forward()
     
    except(KeyboardInterrupt):
        kill_power()



def sensor():
    i = GPIO.input(21)
    if i== 0:
        print("obstacle detected on left {}".format(i))
        reverse()


def kill_power():
    print("killing power") 
    GPIO.output(17, False)
    GPIO.output(18, False)
    GPIO.output(20, False)
    GPIO.output(26, False)
    quit()


if __name__ == "__main__":
    print("main was called")
    drive = True

    try:

        while drive:
            drive_forward()
            drive = sensor()
        kill_power()


    except(KeyboardInterrupt,  ValueError):
        print('finishing up')
        kill_power()

