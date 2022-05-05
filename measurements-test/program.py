import RPi.GPIO as GPIO
import time
import smbus2
import numpy as np
import threading

from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

bus = smbus2.SMBus(1)
adr = 0x6a

GPIO.setmode(GPIO.BCM)

def read_sensor():
    x = np.int16(bus.read_word_data(adr, 0x28))
    y = np.int16(bus.read_word_data(adr, 0x2A))
    z = np.int16(bus.read_word_data(adr, 0x2C))
    return [x,y,z]


token = "ESYZerRr38vwWAlKs3gm8Je_Msc-wEQs11uoIWwYCAzIPjnKFSU8bdG-2jAuqSSE5Sr9ZVcZSvajmFYup9zT7A=="
org = "initorg"
bucket = "measurementsbucket"


period:int =  1000000/5 #Okres w nanosekundach

with InfluxDBClient(url="127.0.0.1:8086", token=token, org=org) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)

def write_to_influx(tablename:str,acc_x:int,acc_y:int,acc_z:int):
    point = Point(tablename) \
    .field("acc_x", acc_x) \
    .field("acc_y", acc_y) \
    .field("acc_z", acc_z) \
    .time(datetime.utcnow(), WritePrecision.US)

    write_api.write(bucket, org, point)


bus.write_byte_data(adr, 0x01, 0b00000000)  # FUNC_CFG_ACCESS (01h)
bus.write_byte_data(adr, 0x04, 0b00000001)  # SENSOR_SYNC_TIME_FRAME (04h)

bus.write_byte_data(adr, 0x10, 0b10100000)  # CTRL1_XL (10h) Acc f [Hz] 208
bus.write_byte_data(adr, 0x11, 0b00000100)  # CTRL2_G (11h)

time_interrupt_flag:bool = False

last_time = time.time_ns()
try:
    while True:
        actual_time = time.time_ns()
        if actual_time - last_time > period:
            last_time = actual_time
            measures = read_sensor()
            write_to_influx("acc_test3",measures[0],measures[1],measures[2])  
except:
    GPIO.cleanup()
    client.close()

    
