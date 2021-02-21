from time import sleep
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1015(address=0x48,busnum = 1)


GAIN = 2/3

#Main loop.
while 1:
    value = [0]

    value[0] = adc.read(0, gain = GAIN)	

    volts = value[0] / 2074 * 6.144

    sleep(1)
