import numpy as np
import time 
import threading
import RPi.GPIO as GPIO


ledPin=21
buttonPin=16

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def time_interrupt():
    print(time.ctime())
    threading.Timer(10, time_interrupt).start()
    

time_interrupt()
try:
    while(1):
        button_state = GPIO.input(buttonPin)
        if button_state == GPIO.HIGH:
            print("Button high")
            GPIO.output(ledPin, GPIO.HIGH)
        else:
            print("Button low")
            GPIO.output(ledPin, GPIO.LOW)
        time.sleep(0.1)
except:
    GPIO.cleanup()

    
