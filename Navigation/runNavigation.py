import openpyxl
import time
from findNavigation import *
import subprocess
from Arduino import *

#neighboorsDictionary = getNeighboors(neighboors)
londonDataDictionary = getLondonData(london)#, neighboorsDictionary)
roadStatusDictionary = getRoadStatus(london)
#print roadStatusDictionary

'''
start = '331357'
goal = '8653432'

shortestPath = findshortestPath(start, goal, londonDataDictionary)
environmentPath = findPathEnvironment(londonDataDictionary, shortestPath)
'''
#for testing
environmentPath = ['331357', '2496401', '2496401', '331357', '2496401', '2496401', '331357', '2495383', '2495401',  '331357', '2496402', '2498957']

#environmentPath = ['331357', '2495341', '2495342', '2495343', '2495344', '2495380', '2495382', '2495383', '2495401', '2496401', '2496402', '249895']


for i in range(len(environmentPath)):
    #print i
    color = roadStatusDictionary[environmentPath[int(i)]].color
    #navigation = londonDataDictionary[environmentPath].streetName
    navigation= "streetname"
    ArduinoRun(color, navigation)
    #while True:
    #   time.sleep(3)   # Delay for 1 minute (7 seconds).