import serial # you need to install the pySerial :pyserial.sourceforge.net
import time
# your Serial port should be different!
arduino = serial.Serial('/dev/tty.usbmodem1411', 9600)

def onOffFunction(counter):
    command = 'on'
      #raw_input("Type something..: (on/ off / bye )");
    if command =="on" and counter<=5:
        print counter
        print "The LED is on..."
        time.sleep(1)
        arduino.write('H')
        counter += 1
        onOffFunction(counter)

    elif command =="off":
        print "The LED is off..."
        time.sleep(1)
        arduino.write('L')
        onOffFunction()
        arduino.close()
    elif command =="bye":
        print "See You!..."
        time.sleep(1)
        arduino.close()
    else:
        print "Sorry..type another thing..!"
        onOffFunction()

time.sleep(2) #waiting the initialization...



onOffFunction(0)