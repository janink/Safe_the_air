from pyfirmata import Arduino, util
import time
ard = Arduino('/dev/cu.usbmodem1411')





def onOffFunction(command):

    if command =="G":
        ard.digital[8].write(1)
        time.sleep(5)
        ard.digital[8].write(0)
        pass
    elif command == "Y":
        ard.digital[10].write(1)
        time.sleep(5)
        ard.digital[10].write(0)

    elif command == "R":
        ard.digital[12].write(1)
        time.sleep(5)
        ard.digital[12].write(0)
    else:
        ard.digital[8].write(0)



def streetNameShow(streetname):
    LCD(streetname)

def ArduinoRun(color, streetname):
    onOffFunction(color)
    streetNameShow(streetname)



ArduinoRun('Y', 'street1')