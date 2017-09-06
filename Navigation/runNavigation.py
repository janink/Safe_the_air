import openpyxl
import time
from findNavigation import *
import subprocess
from Arduino import *

#neighboorsDictionary = getNeighboors(neighboors)
londonDataDictionary = getLondonData(london)#, neighboorsDictionary)
roadStatusDictionary = getRoadStatus(london)

'''
start = '331357'
goal = '8653432'

shortestPath = findshortestPath(start, goal, londonDataDictionary)
environmentPath = findPathEnvironment(londonDataDictionary, shortestPath)
'''
#for testing
environmentPath = ['331357', '2495341', '2495342', '2495343', '2495344', '2495380', '2495382', '2495383', '2495401', '2496401', '2496402', '2498957', '2498964', '2498965', '2498997', '2499055', '2499065', '2499080', '2499081', '2499180', '2499181', '2499182', '2499578', '2499579', '2499581', '2499582']
color = ['Y','G','G','Y','G','G','Y']


#for i in range(len(environmentPath)):
for i in color:
    print i
    #color = roadStatusDictionary[environmentPath].color
    #navigation = londonDataDictionary[environmentPath].streetName
    navigation= "streetname"
    ArduinoRun(i, navigation)
    #while True:
    #   time.sleep(3)   # Delay for 1 minute (7 seconds).