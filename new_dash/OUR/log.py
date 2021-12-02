import csv, os
from config import *
# Function to create a csv with the specified header.

# Debug function to read from log file for GUI testing.
def readLog(logFile):
    with open(logFile, 'r') as f:
        reader = csv.reader(f)
        logList = list(reader)
    return logList

speed = 0
speedo_iter = 0
intakeTemp = 0
batt_level = 0
sensor = 0
pedal = 0
batt_v = 0
batt_temp = 0
# Debug function that reads from log file and assigns to global values
def getLogValues(logFile):
    global logIter
    global speed
    global speedo_iter
    global intakeTemp
    global batt_level
    global sensor
    global pedal
    global batt_v
    global can
    global voltage
    global batt_temp
    speed = int((logFile[logIter][1]))
    speedo_iter = int((speed)/5)
    coolantTemp = logFile[logIter][2]
    intakeTemp = logFile[logIter][3]
    throttlePosition = logFile[logIter][4]
    engineLoad = logFile[logIter][5]
    batt_level = logFile[logIter][6]
    sensor = logFile[logIter][7]
    pedal = logFile[logIter][8]
    batt_v = logFile[logIter][9]
    can = logFile[logIter][10]
    voltage = logFile[logIter][11]
    batt_temp = logFile[logIter][12]
    logIter += 1
    # Reset iterator.
    if logIter == logLength:
        logIter = 1
