import serial

def reading():
    global answer
    answer = ser.readline()
    print(answer)

def writing(ask):
    ser.write(ask)
    print('command -', ask)


connected = False
try:
    ser = serial.Serial("COM6", 115200)
except serial.serialutil.SerialException:
    ser = serial.Serial("COM11", 115200)


while not connected:
    serin = ser.read()
    connected = True


while ser.read():
    reading()
    if answer == b'\r\n':
        writing(1)

ser.close()