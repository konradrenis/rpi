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
    return [x,y,z]



bus.write_byte_data(adr, 0x01, 0b00000000)  # FUNC_CFG_ACCESS (01h)
bus.write_byte_data(adr, 0x04, 0b00000100)  # SENSOR_SYNC_TIME_FRAME (04h)
#bus.write_byte_data(adr, 0x06, 0b00000000)  # FIFO_CTRL1 (06h)
#bus.write_byte_data(adr, 0x07, 0b00000000)  # FIFO_CTRL2 (07h)
#bus.write_byte_data(adr, 0x08, 0b00000000)  # FIFO_CTRL3 (08h)
#bus.write_byte_data(adr, 0x09, 0b00000000)  # FIFO_CTRL4 (09h)
#bus.write_byte_data(adr, 0x0A, 0b00000000)  # FIFO_CTRL5 (0Ah)
#bus.write_byte_data(adr, 0x0B, 0b00000000)  # ORIENT_CFG_G (0Bh)
#bus.write_byte_data(adr, 0x0D, 0b00000000)  # INT1_CTRL (0Dh)
#bus.write_byte_data(adr, 0x0E, 0b00000000)  # INT2_CTRL (0Eh) 
#Wazne
bus.write_byte_data(adr, 0x10, 0b01011010)  # CTRL1_XL (10h) Acc f [Hz] 208
bus.write_byte_data(adr, 0x11, 0b01010110)  # CTRL2_G (11h)
#
#bus.write_byte_data(adr, 0x12, 0b00000100)  # CTRL3_C (12h)
#bus.write_byte_data(adr, 0x13, 0b00000000)  # CTRL4_C (13h)
#bus.write_byte_data(adr, 0x14, 0b00000000)  # CTRL5_C (14h) 
#bus.write_byte_data(adr, 0x15, 0b00000000)  # CTRL6_C (15h)
#bus.write_byte_data(adr, 0x16, 0b00000000)  # CTRL7_G (16h)
#bus.write_byte_data(adr, 0x17, 0b00000000)  # CTRL8_XL (17h)
#bus.write_byte_data(adr, 0x18, 0b00111000)  # CTRL9_XL (18h)
#bus.write_byte_data(adr, 0x19, 0b00111000)  # CTRL10_C (19h)

#bus.write_byte_data(adr, 0x1A, 0b00000000)  # MASTER_CONFIG (1Ah)



while True:
    time.sleep(0.3)
    print('[X Y Z] = ' + str(read()))
    
