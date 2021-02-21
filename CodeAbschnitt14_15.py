import time
from time import sleep
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1015(address=0x48,busnum=1)
import RPi.GPIO as GPIO
import os
import sys
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

pid = str(os.getpid())
pidfile = "/tmp/ml_klassif.pid"
open(pidfile, 'w').write(pid)

fileObject=open("isMLIrrigation.txt","r")
tmp = fileObject.read()
if(tmp == "0"):
    GPIO.cleanup()
    sys.exit()

p_max = 1272
p_min = 642
one_perc = (p_max-p_min) /100
percentage =0
GAIN = 2/3
t_end = time.time() + 5
temp = 0
GAIN = 2/3
while time.time() < t_end:
    value = [0]
    value[0] = adc.read_adc(0,gain=GAIN)
    temp = temp + value[0]
    sleep(0.2)
    
percentage = 100 - ((temp/25) -p_min)/one_perc
if (percentage > 100):
    percentage = 100
if (percentage < 0) : 
    percentage = 0

try:
    fileObject=open("ML_report.txt","r")
    if(fileObject.read() == "['ON']") and (percentage < 80):
            GPIO.output(11, GPIO.LOW)
            sleep(5)
            GPIO.output(11, GPIO.HIGH)
            fileObject.close()
    else:
        GPIO.output(11, GPIO.HIGH)
        fileObject.close()     
finally:
    GPIO.cleanup()
    os.unlink(pidfile)
