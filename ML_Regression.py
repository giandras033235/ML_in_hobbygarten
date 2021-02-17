import RPi.GPIO as GPIO
import os
import sys
import time
import re
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
nums = [0,1,2,3,4,5,6,7,8,9]
sol = ""
pid = str(os.getpid())
pidfile = "/tmp/ml_regression.pid"
open(pidfile, 'w').write(pid)

fileObject=open("isMLIrrigation.txt","r")
tmp = fileObject.read()
if(tmp == "0"):
    GPIO.cleanup()
    sys.exit()

try:
    fileObject=open("ML_report.txt","r")
    num = re.split(r'[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)',fileObject.read())[1]
    GPIO.output(11, GPIO.LOW)
    sleep(float(num))
    GPIO.output(11, GPIO.HIGH)
    fileObject.close()

finally:
    GPIO.cleanup()
    os.unlink(pidfile)