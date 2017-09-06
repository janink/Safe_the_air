import openpyxl
import time
from findNavigation import *
import subprocess
from Arduino import *

#neighboorsDictionary = getNeighboors(neighboors)
londonDataDictionary = getLondonData(london)#, neighboorsDictionary)
roadStatusDictionary = getRoadStatus(london)
print roadStatusDictionary

'''
start = '331357'
goal = '8653432'

shortestPath = findshortestPath(start, goal, londonDataDictionary)
environmentPath = findPathEnvironment(londonDataDictionary, shortestPath)
'''
#for testing
environmentPath = ['331357', '2496401', '2496401', '331357', '2496401', '2496401', '331357', '2495383', '2495401', '331357', '2496402', '2498957', '2498964', '2498965', '2496401', '2499055', '2496401', '2499080', '2496401', '2499180', '2499181', '2499182', '2499578', '2499579', '2499581', '2499582']
#color = ['Y','G','G','Y','G','G','Y']


for i in range(len(environmentPath)):
    print i
    color = roadStatusDictionary[environmentPath[int(i)]].color
    #navigation = londonDataDictionary[environmentPath].streetName
    navigation= "streetname"
    ArduinoRun(color, navigation)
    #while True:
    #   time.sleep(3)   # Delay for 1 minute (7 seconds).