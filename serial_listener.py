import os
import serial
import time

serial_port = 'COM3'
ser = None
connected = False

def try_connect(port):
    try:
        print("Trying to connect to serial port " + port)
        ser = serial.Serial(
            port = port,\
            baudrate = 9600,\
            bytesize = serial.EIGHTBITS,\
            timeout = 3)
        time.sleep(1)
        return True
    except (serial.serialutil.SerialException):
        print("Couldn't connect to serial port " + port)
        return False

while not connected:
    connected = try_connect(serial_port)
    if not connected:
        user_input = input("Retry connection now? (y/n):")
        if user_input.lower() == "y":
            continue
        else:
            exit()

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
