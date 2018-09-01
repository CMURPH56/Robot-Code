import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    i = GPIO.input(40)
    if i== 0:
        print("Obstacle detected on left {}".format(i))
        time.sleep(0.1)
