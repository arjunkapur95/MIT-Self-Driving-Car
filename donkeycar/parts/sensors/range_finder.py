# Contributers: Joseph R. , Mahsa B. and Kevin P.

# FOR Rasberry Pi Model 3 v1.###

# This script starts up the ultrasonic sensor and returns a distance from an object

# NOTE: TRIG and ECHO values reference the physical GPIO pin it is connected on the Rpi
#		If pin layout is re-arranged, the script must be updated to reflect changes

# TODO: Adjust timing for donkey car application (Detecting objects in front of it)
# 		Proposed query distance, at least 15cm to 20cm

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 20 # Changed
ECHO = 21 # Changed

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(2) #Can be ajusted for quicker distance queries

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
  pulse_start = time.time()

while GPIO.input(ECHO)==1:
  pulse_end = time.time()

pulse_duration = pulse_end - pulse_start
          
distance = pulse_duration * 17150
          
distance = round(distance, 2) 
        
print "Distance:",distance,"cm"
             
GPIO.cleanup()
