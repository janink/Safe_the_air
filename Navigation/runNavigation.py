import openpyxl
import time
from findNavigation import *
import subprocess
from Ardurino import *

neighboorsDictionary = getNeighboors(neighboors)
londonDataDictionary = getLondonData(london, neighboorsDictionary)
roadStatusDictionary = getRoadStatus(london)

start = '331357'
goal = '8653432'

shortestPath = findshortestPath(start, goal, londonDataDictionary)
environmentPath = findPathEnvironment(londonDataDictionary, shortestPath)


for i in range(len(environmentPath)):
    color = roadStatusDictionary[environmentPath].color
    navigation = londonDataDictionary[environmentPath].streetName
    ArdurinoRun(color, navigation)    
    while True:
        time.sleep(3)   # Delay for 1 minute (7 seconds).
        
        