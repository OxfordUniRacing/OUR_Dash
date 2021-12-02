#!/usr/bin/python
import ecu
import datetime
import numpy as np

# Globals.
logLength = 0
dtc_iter = 0
time_elapsed_since_last_action = 0
gui_test_time = 600
logIter = 1
ecuReady = False
debugFlag = True
piTFT = True
startTime = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
RESOLUTION = (480, 272)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# LUT representing the speeds at each of the five gears. Each entry is +200 RPM, and
# is directly linked to rpmList.


# List of RPM values for above LUT.
