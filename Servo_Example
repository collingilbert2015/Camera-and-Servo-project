#!/usr/bin/python
from Adafruit_PWM_Servo_Driver import PWM
import time
from flask import Flask, render_template, request
# ===========================================================================
#                       COLLIN'S FREAKIN' AWESOME WEBCAM APP THING
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)

# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

#Create app name from flask 

app = Flask(__name__)

currentDirection = 0

pwm.setPWMFreq(60)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
angle = { 'servo' : { 'name' : 'pan', 'angle': 0 }}

#----------------------------------------------------------------------------
#Render Template 
timeString = time.strftime("%H:%M:%S")


@app.route("/")

def main():
        template_Data = {
        'title' : 'AWESOME',
        "time"  : timeString
        }
        return render_template('main.html', **template_Data)

#----------------------------------------------------------------------------
#ROUTE
@app.route("/<direction>")
def move(direction):
        global currentDirection
        if direction == 'left':
                pwm.setPWM(0, 0, servoMax)
                time.sleep(.02)
        }
        return render_template('main.html', **template_Data)

#----------------------------------------------------------------------------
#ROUTE
@app.route("/<direction>")
def move(direction):
        global currentDirection
        if direction == 'left':
                pwm.setPWM(0, 0, servoMax)
                time.sleep(.02)
                cleanup()
                currentDirection +=1
                print currentDirection
        elif direction == 'right':
                pwm.setPWM(0, 0, servoMin)
                time.sleep(.02)
                cleanup()
                currentDirection -= 1
                print currentDirection

          elif direction == 'return':
                if(currentDirection > 0 ):
                        while(currentDirection > 0):
                                pwm.setPWM(0, 0, servoMin)
                                time.sleep(.02)
                                cleanup()
                                currentDirection -= 1
                                print currentDirection
                                time.sleep(3)
          elif(currentDirection < 0):
                        while(currentDirection < 0):
                                pwm.setPWM(0,0, servoMax)
                                time.sleep(.02)
                                cleanup()
                                currentDirection += 1
                                print currentDirection
    time.sleep(3)
                elif(currentDirection < 0):
                        while(currentDirection < 0):
                                pwm.setPWM(0,0, servoMax)
                                time.sleep(.02)
                                cleanup()
                                currentDirection += 1
                                print currentDirection
                                time.sleep(3)
        return "ok"

#-----------------------------------------------------------------------------
def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 100
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

#----------------------------------------------------
def cleanup():
        pwm.setPWM(0,0,0)
#-----------------------------------------------------------------------------
# +++++++++++++++++++++RETURN FUNCTION+++++++++++++++++++++++++++++++++++++++
#-----------------------------------------------------------------------------


#----------------------------------------------------
if __name__ == "__main__":
        app.run(host = '0.0.0.0', port = 80, debug = False)
