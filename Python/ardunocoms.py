import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout =1)
    ser.reset_input_buffer()

    missionName = input("Mission name: ")
    file = open(f"/home/tim-t/Documents/missions/{missionName}.txt", "w")
    tl = time.localtime()
    tz = time.gmtime()
    formatTime = time.strftime('%H:%M', tl)
    formatTimez = time.strftime('%H%M', tz)
    date = time.strftime('%d %b %y', tz)


    file.write(f"date: {date} \n")
    file.write(f"File created at {formatTime} | {formatTimez}\n")
    file.close


    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            servo1position = line[1:4]
            servo2position = line[4:]
            print(f'servo one = {servo2position}')
