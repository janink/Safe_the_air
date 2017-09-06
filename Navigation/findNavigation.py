import openpyxl
import pickle
from scipy.spatial import distance
import math

excelFile = 'LondonStreetData.xlsx'
data = openpyxl.load_workbook(excelFile)
london = data.get_sheet_by_name('london')

excelFile = 'LondonStreetNeighboorData.xlsx'
data = openpyxl.load_workbook(excelFile)
neighboors = data.get_sheet_by_name('neighboors')

class London:
    def __init__(self, streetID, streetName, area, roadStatus, neighboors, lat, long):
        self.streetID = streetID
        self.streetName = streetName
        self.area = area
        self.roadStatus = roadStatus
        self.neighboors = neighboors
        self.lat = lat
        self.long = long

class Roadstatus:
    def __init__(self, color):
        self.color = color

class Neighboor:
    def __init__(self, hasNeighboor):
        self.hasNeighboor = hasNeighboor
        
def getNeighboors(sheet):
    try:
        with open("pickle/neighboorsDictionary.txt", "rb") as myFile:
            neighboorsDictionary = pickle.load(myFile)
    except:
        neighboorsDictionary, neighboorsList = {}, []
        for i in range(2, sheet.max_row+1):
            neighboorsList.append(sheet['B'+str(i)].value)
            if sheet['A'+str(i)].value != sheet['A'+str(i+1)].value:
                neighboorsDictionary[sheet['A'+str(i)].value] =  Neighboor(neighboorsList)
                neighboorsList = []
        with open("pickle/neighboorsDictionary.txt", "wb") as myFile:
            pickle.dump(neighboorsDictionary, myFile)
    return neighboorsDictionary

def getLondonData(sheet):
    try:
        with open("pickle/londonDataDictionary.txt", "rb") as myFile:
            londonDataDictionary = pickle.load(myFile)
    except:
        londonDataDictionary = {}
        for i in range(2, sheet.max_row+1):
            
        with open("pickle/londonDataDictionary.txt", "wb") as myFile:
            pickle.dump(londonDataDictionary, myFile)
    return londonDataDictionary

def getRoadStatus(sheet):
    try:
        with open("pickle/roadStatusDictionary.txt", "rb") as myFile:
            roadStatusDictionary = pickle.load(myFile)
    except:
        roadStatusDictionary = {}
        listOptions = [None, 'green', 'yellow', 'red']
        for i in range(2, sheet.max_row+1):
            if 
            roadStatusDictionary[sheet['A'+str(i)].value]
        with open("pickle/roadStatusDictionary.txt", "wb") as myFile:
            pickle.dump(roadStatusDictionary, myFile)
    return roadStatusDictionary

def getClosestNeighboor(neighboors, point, goalLat, goalLong, londonData):
    closestNeighboor = point
    closestDistance = math.inf
    for i in range(len(neighboors)):
        a = (londonData[neighboors[i]].lat, goalLat)
        b = (londonData[neighboors[i]].long, goalLong)
        dst = distance.euclidean(a,b)
        if closestDistance > dst:
            closestDistance = dst
            closestNeighboor = neighboors[i]
    return closestNeighboor   
    
def findshortestPath(start, goal, londonData):
    pathList = [start]
    goalLat = londonData[goal].lat
    goalLong = londonData[goal].long
    point = start
    while point != goal:
        if goal in londonData[point].neighboors:
            break
        closestNeighboor = getClosestNeighboor(londonData[point].neighboors, point, goalLat, goalLong, londonData)      
        pathList.append(closestNeighboor)
        point = closestNeighboor
    pathList.append(goal)
    return pathList


def findAlternativePathPart():
    
    return

def findPathEnvironment(start, goal, londonData, shortestPath):
    
    return pathList


#-------------------------run---------------------------------------

neighboorsDictionary = getNeighboors(neighboors)
londonDataDictionary = getLondonData(london)
roadStatusDictionary = getRoadStatus(london)

start = startID #= roadID 331357
goal = goalID #= roadID 8653432

shortestPath = findPath(startID, goalID, londonDataDictionary)
environmentPath = findPathEnvironment(startID, goalID, londonDataDictionary, shortestPath)
