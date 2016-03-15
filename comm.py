import serial



try:
    output = ''
    ser = serial.Serial("/dev/tty.usbserial-A50285BI", 115200, timeout=1)
    # ser.open()
    if not ser.open:
        ser.open()
    while True:
        ser.reset_input_buffer()  # clear all the junk
        ser.write(b'1\n')
        line = ser.read()
        while line != '\n':
            output += line
            line = ser.read()
        print output
except Exception as e:
    ser.close()
    print e



