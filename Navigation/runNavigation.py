import openpyxl
import time
from findNavigation import *
import subprocess
from Ardurino import *

neighboorsDictionary = getNeighboors(neighboors)
londonDataDictionary = getLondonData(london)
roadStatusDictionary = getRoadStatus(london)

start = startID #= roadID 331357
goal = goalID #= roadID 8653432

shortestPath = findPath(startID, goalID, londonDataDictionary)
environmentPath = findPathEnvironment(startID, goalID, londonDataDictionary, shortestPath)


for i in range(len(environmentPath)):
    color = roadStatusDictionary[environmentPath].color
    navigation = londonDataDictionary[environmentPath].streetName
    ArdurinoRun(color, navigation)    
    while True:
        time.sleep(7)   # Delay for 1 minute (7 seconds).
        
        