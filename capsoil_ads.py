import board
import busio
import adafruit_ads1x15.ads1015 as ADS
import RPi.GPIO as GPIO

from time import sleep

i2c = busio.I2C(board.SCL, board.SDA)

from adafruit_ads1x15.analog_in import AnalogIn
ads = ADS.ADS1015(i2c)
chan0 = AnalogIn(ads, ADS.P0)

while True:
    
    print('Channel 0 is:',chan0.value, chan0.voltage)
    #print('Channel 1 is:',chan1.value, chan1.voltage)
    sleep(1)