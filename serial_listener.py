import os
import serial
import time

ser = serial.Serial(
    port = 'COM3',\
    baudrate = 9600,\
    bytesize = serial.EIGHTBITS,\
    timeout = 3)

time.sleep(1)

print("connected to serial on port: " + ser.portstr)

audio_devices = ["Speakers", "Headset Earphone"]
current_device = 0 #default this to first element. If not this, pressing button one additional time will be needed


while True:
    serial_string = str(ser.readline())
    serial_string = serial_string.strip("b'")
    serial_string = serial_string.strip("\\r\\n")

    if serial_string == "p":
        if current_device == (len(audio_devices) - 1):
            current_device = 0
        else:
            current_device += 1
        print("Switching to: " + audio_devices[current_device])
        os.system("nircmd.exe setdefaultsounddevice \"" + audio_devices[current_device] + "\"")
