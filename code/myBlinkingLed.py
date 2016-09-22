#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
def Blink():
	while True:
		time.sleep(1)
                print "...."
                time.sleep(1)
                print "...."
		for i in range(0,3):
			 print "blink" + str(i + 1)
			 GPIO.output(17,True)
			 time.sleep(.25)
			 GPIO.output(17,False)
			 time.sleep(.25)
			 print "done!!"
                 	
	 	time.sleep(1)
		print "...."
		time.sleep(1)
		print "...."
		time.sleep(1)
		print "...."
		time.sleep(1)
		print "...."
		time.sleep(1)
		print "...." 
		for x in range(0,5):
                         print "blink" + str(x + 1) 
			 GPIO.output(17,True)
                         time.sleep(.25)
                         GPIO.output(17,False)
                         time.sleep(.25)
                         print "done!!"

Blink()
