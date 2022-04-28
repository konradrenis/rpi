from datetime import datetime


a = datetime.strptime('2022-04-28T11:52:33.375392Z', '%Y-%m-%dT%H:%M:%S.%fZ')
print(a.nanosecond)