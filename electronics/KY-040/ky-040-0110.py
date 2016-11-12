#!/usr/bin/env python

#
#
# not currently working
#
#

# External module imports
import RPi.GPIO as GPIO
import time

val=0

# Pin Definitons:

aPin = 20
bPin = 21

cPin = 16

lastA = 0
lastB = 0



def encoderswitch(pin):
    print ('switch', pin)

def encodercount(pin):
    global val
    global lastA
    global lastB
    
    dir=GPIO.input(bPin)
    print pin, dir

    if pin==aPin:
        lastA=dir

    if pin==bPin:
        lastB=dir

    if lastA==1 and lastB == 1:
            print "--"
    
#    if GPIO.input(bPin)==0:
#      dir="U"
#      if val<20:
#        val+=1
#      #print "inc"
#    else:
#      dir="D"
#      if val>0:
#        val-=1
#        #print "dec"

#    print dir, val

# Pin Definitons:
#cPin = 16 
#aPin = 20
#bPin = 21

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

GPIO.setup(aPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 
GPIO.setup(bPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #

GPIO.setup(cPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # 

# Initialize the interrupts - these trigger on the both the rising and falling 
GPIO.add_event_detect(cPin, GPIO.FALLING, callback = encoderswitch, bouncetime=250)   # Encoder Button

#GPIO.add_event_detect(aPin, GPIO.RISING, callback = encodercount, bouncetime=5)   # Encoder A
#GPIO.add_event_detect(aPin, GPIO.RISING, callback = encodercount)   # Encoder A

GPIO.add_event_detect(aPin, GPIO.BOTH, callback = encodercount)   # Encoder A
GPIO.add_event_detect(bPin, GPIO.BOTH, callback = encodercount)   # Encoder B

hist = "2222"
print "1) ",hist
hist += "a"
hist = hist[1:5]
print "2) ",hist
hist += "b"
hist = hist[1:5]
print "2) ",hist
hist += "c"
hist = hist[1:5]
print "2) ",hist
hist += "d"
hist = hist[1:5]
print "2) ",hist


print ("Here we go! Press CTRL+C to exit")
try:
    while 1:
        time.sleep(0.01)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.remove_event_detect(aPin) # remove event
    GPIO.remove_event_detect(cPin) # remove event
    GPIO.cleanup() # cleanup all GPIO
