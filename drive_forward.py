import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.IN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT) # Left Forward
GPIO.setup(18, GPIO.OUT) # Left Backward
GPIO.setup(20, GPIO.OUT) # Right Forward
GPIO.setup(26, GPIO.OUT) # Right Backward




try:
    while True:
        GPIO.output( 17, True)
        GPIO.output( 18, False)
        GPIO.output( 20, True)
        GPIO.output( 26, False)
except(KeyboardInterrupt):
    GPIO.output( 17, False)
    GPIO.output( 18, False)
    GPIO.output( 20, False)
    GPIO.output( 26, False)
    quit()
