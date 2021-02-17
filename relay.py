import time
import RPi.GPIO as GPIO

     
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(11,GPIO.OUT)
GPIO.output(11, GPIO.LOW)

time.sleep(5)

GPIO.output(11, GPIO.HIGH)
GPIO.cleanup()

