import serial
import json



try:
    output = ''
    ser = serial.Serial("/dev/tty.usbserial-A50285BI", 115200, timeout=1)
    # ser.open()
    if not ser.open:
        ser.open()
    timestamp = 0
    feed = 0
    while True:
        # clear all the junk
        # ser.reset_input_buffer()
        # ser.reset_output_buffer() 
        print b'{}\n'.format(feed)
        ser.write(b'{}\n'.format(feed))
        feed += 1
        if feed == 10:
            feed = 0

        line = ser.read()
        while line != '\n':
            output += line
            line = ser.read()
        print output + ' '
        print '\n\n\n\n\n'
        timestamp += 1
        dic_me = json.loads(output)
        print dic_me
        output = ''
except Exception as e:
    ser.close()
    print e



