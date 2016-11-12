#!/usr/bin/env python

# External module imports
import RPi.GPIO as GPIO
import time

val=0

# Pin Definitons:

aPin = 20 # clock
bPin = 21 # data/direction

cPin = 16

def encoderswitch(pin):
    print ('switch', pin)

def encodercount(pin):
    global val
    
##    dir=GPIO.input(bPin)

    if GPIO.input(bPin)==0:
      # Increment
      dir="U"
      if val<30:
        val+=1
    else:
      # Decrement
      dir="D"
      if val>00:
        val-=1

    print dir, val

# Pin Definitons:
#cPin = 16 
#aPin = 20
#bPin = 21

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

GPIO.setup(aPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # 
GPIO.setup(bPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #
GPIO.setup(cPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # 


# Initialize the interrupts - these trigger on the both the rising and falling 
GPIO.add_event_detect(aPin, GPIO.FALLING, callback = encodercount)   # Encoder A
#GPIO.add_event_detect(bPin, GPIO.BOTH, callback = encodercount)   # Encoder B (not required)
GPIO.add_event_detect(cPin, GPIO.FALLING, callback = encoderswitch, bouncetime=50)   # Encoder C

print ("Here we go! Press CTRL+C to exit")
try:
    while 1:
        time.sleep(0.01)
        #time.sleep(0.10)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.remove_event_detect(aPin) # remove event
    GPIO.remove_event_detect(cPin) # remove event
    GPIO.cleanup() # cleanup all GPIO
