from time import sleep
import Adafruit_ADS1x15
import os
import sys
adc = Adafruit_ADS1x15.ADS1015(address=0x48,busnum=1)
import RPi.GPIO as GPIO
import psutil


p_max = 1272
p_min = 642
one_perc = (p_max-p_min) /100
percentage =0

GAIN= 2/3

        
fileObject = open("isAutonumous.txt", "w")
fileObject.write(str(1))
fileObject.close()
if (os.path.isfile("/tmp/ml_klassif.pid") or  os.path.isfile("/tmp/ml_regression.pid")):
     print("Another Program is Running")
     sleep(2)
     print("\n")
     sys.exit()

    
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

while 1:
        fileObject=open("isAutonumous.txt","r")
        if(fileObject.read() == "0"):
            fileObject.close()
            break
        fileObject.close()
        value = [0]
        value[0] = adc.read_adc(0,gain=GAIN)
        percentage = 100 - (value[0] -p_min)/one_perc
        if (percentage > 100):
            percentage = 100
        if (percentage < 0) : 
            percentage = 0
        if percentage < 80 :
            GPIO.output(11, GPIO.LOW)
        else :
            GPIO.output(11, GPIO.HIGH)

        volts = value[0] / 2047.0 * 6.144
       # print("{0:0.3f}V [{1}]  [{2:0.2f}] %".format(volts, value[0] , percentage))
        sleep(1)

GPIO.cleanup()
 