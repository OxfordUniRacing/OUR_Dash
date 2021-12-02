import config
from threading import Thread
import obd
import numpy as np
# Globals

global speed
speed = 10

coolantTemp = 5
intakeTemp = 0
MAF = 0
throttlePosition = 0
speedo_iter = 50
timingAdvance = 0
engineLoad = 0
connection = None
   
class ecuThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        global connection
        ports = obd.scan_serial()
        print(ports)
        # DEBUG: Set debug logging so we can see everything that is happening.
        obd.logger.setLevel(obd.logging.DEBUG)

        # Connect to the ECU.
        connection = obd.Async("/dev/ttyUSB0", 115200, "3", fast=False)
        # Watch everything we care about.
        connection.watch(obd.commands.SPEED, callback=self.new_speed)
        connection.watch(obd.commands.COOLANT_TEMP,\
        callback=self.new_coolant_temp)
        connection.watch(obd.commands.INTAKE_TEMP,\
        callback=self.new_intake_temp)
        connection.watch(obd.commands.MAF, callback=self.new_MAF)
        connection.watch(obd.commands.THROTTLE_POS,\
        callback=self.new_throttle_position)
        connection.watch(obd.commands.ENGINE_LOAD,\
        callback=self.new_engine_load)

        
        # Start the connection.
        connection.start()
        
        # Set the ready flag so we can boot the GUI.
        config.ecuReady = True
#speed, distance, battery, battery temperature, motor temperature
   