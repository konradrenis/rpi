import RPi.GPIO as GPIO
import time
import smbus2
import numpy as np
from threading import Thread

def read_sensor():
    block = bus.read_i2c_block_data(adr, 0x28, 6)
    return np.array([time.time_ns(), np.int16(block[1] << 8 | block[0]), np.int16(block[3] << 8 | block[2]), np.int16(block[5] << 8 | block[4])])

def save_txt(arr):
    with open('./measurements-test/data.dat', 'a') as f:
        np.savetxt(f, arr, fmt='%d')
        f.close()

bus = smbus2.SMBus(1)
adr = 0x6a

ledPin=16
switchPin=18

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


bus.write_byte_data(adr, 0x01, 0b00000000)  # FUNC_CFG_ACCESS (01h)
bus.write_byte_data(adr, 0x04, 0b00000001)  # SENSOR_SYNC_TIME_FRAME (04h)

bus.write_byte_data(adr, 0x10, 0b10100000)  # CTRL1_XL (10h) Acc f [Hz] 208
bus.write_byte_data(adr, 0x11, 0b00000100)  # CTRL2_G (11h)


ledOn = False

measures = np.empty(shape = [1,4], dtype = np.int16)

try:
    while True:
        switch_state = GPIO.input(switchPin)
        if switch_state == GPIO.HIGH:

            # Zapisywanie, nowy wątek
            measures = np.delete(measures,0,0)
            thread1 = Thread(target = save_txt,args = (measures))
            thread1.start()

            measures = np.empty(shape = [1,4], dtype = np.int16)

            #Zbieranie pomiarow
            for i in range(5000):
                measures = np.vstack([measures,read_sensor()])

            thread1.join() #Dołączenie wątku
            
            #Sygnalizacja pracy
            if ledOn == False:
                GPIO.output(ledPin, GPIO.HIGH)
                ledOn = True
            else:
                GPIO.output(ledPin, GPIO.LOW)
                ledOn = False

        else: #Sygnalizacja pracy
            if ledOn == False:
                GPIO.output(ledPin, GPIO.HIGH)
                ledOn = True

except:
    GPIO.cleanup()
    print("?")

    
