from cmath import sqrt
from re import X
import RPi.GPIO as GPIO
import time
import sys
import smbus2
import numpy as np

bus = smbus2.SMBus(1)
adr = 0x6a

def read():
    x = np.int16(bus.read_word_data(adr, 0x28))
    y = np.int16(bus.read_word_data(adr, 0x2A))
    z = np.int16(bus.read_word_data(adr, 0x2C))

    vector = np.array([x,y,z],dtype='float64')

    xscale = np.float64(1)
    yscale = np.float64(1)
    zscale = np.float64(1)

    scale = np.array([xscale, yscale, zscale],dtype = 'float64')

    xminus = np.float64(0)
    yminus = np.float64(0)
    zminus = np.float64(0)
    
    minus = np.array([xminus, yminus, zminus],dtype = 'float64')

    return scale * (vector - minus)

bus.write_byte_data(adr, 0x01, 0b00000000)  # FUNC_CFG_ACCESS (01h)
bus.write_byte_data(adr, 0x04, 0b00000100)  # SENSOR_SYNC_TIME_FRAME (04h)
bus.write_byte_data(adr, 0x10, 0b01011010)  # CTRL1_XL (10h) Acc f [Hz] 208
bus.write_byte_data(adr, 0x11, 0b01010110)  # CTRL2_G (11h)

n = 60
suma = 0
for i in range(n):
    time.sleep(0.01)
    wektor = read()
    m = np.linalg.norm(wektor)
    suma += m/n
print(suma)

