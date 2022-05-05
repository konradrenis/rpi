import RPi.GPIO as GPIO
import time
import smbus2
import numpy as np
import datetime
from datetime import datetime

bus = smbus2.SMBus(1)
adr = 0x6a

GPIO.setmode(GPIO.BCM)

def read_sensor():
    x = np.int16(bus.read_word_data(adr, 0x28))
    y = np.int16(bus.read_word_data(adr, 0x2A))
    z = np.int16(bus.read_word_data(adr, 0x2C))
    return np.array([x,y,z])

def read_sensor2():
    block = bus.read_i2c_block_data(adr, 0x28, 6)
    return [np.int16(block[1] << 8 | block[0]), np.int16(block[3] << 8 | block[2]), np.int16(block[5] << 8 | block[4])]

period:int =  1000000/5 #Okres w nanosekundach


bus.write_byte_data(adr, 0x01, 0b00000000)  # FUNC_CFG_ACCESS (01h)
bus.write_byte_data(adr, 0x04, 0b00000001)  # SENSOR_SYNC_TIME_FRAME (04h)

bus.write_byte_data(adr, 0x10, 0b10100000)  # CTRL1_XL (10h) Acc f [Hz] 208
bus.write_byte_data(adr, 0x11, 0b00000100)  # CTRL2_G (11h)


last_time = time.time_ns()


try:
    while True:
        actual_time:int = datetime.now().time()

        #if actual_time - last_time > period:
            #last_time = actual_time
        measures = read_sensor2()
        with open('./measurements-test/data.dat', 'a') as f:
            f.write('\n' + str(actual_time) +' '+ str(measures))
            f.close()     
except:
    GPIO.cleanup()
    print("?")

    
