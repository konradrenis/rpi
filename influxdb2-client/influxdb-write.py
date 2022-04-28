from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "ESYZerRr38vwWAlKs3gm8Je_Msc-wEQs11uoIWwYCAzIPjnKFSU8bdG-2jAuqSSE5Sr9ZVcZSvajmFYup9zT7A=="
org = "initorg"
bucket = "measurementsbucket"

with InfluxDBClient(url="http://192.168.1.39:8086", token=token, org=org) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)

point = Point("mem1") \
.tag("sensor", "2") \
.field("temperatura", 36) \
.field("cisnienie", 29) \
.field("wilgotnosc", 25) \
.time(datetime.utcnow(), WritePrecision.US)
print(datetime.utcnow())
<<<<<<< HEAD
#cos mojego
=======

#xxxxxxx

>>>>>>> 689e0c128cfee097208386a7219aa24a8cf3afb8
write_api.write(bucket, org, point)


client.close()
