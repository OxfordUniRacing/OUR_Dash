import config, ecu, log, sys
import pygame, os, csv
from pygame.locals import *

# Helper function to draw the given string at coordinate x,y, relative to center.
def drawText(string, x, y, font):
    if font == "readout":
        text = readoutFont.render(string, True, config.WHITE)
    elif font == "label":
        text = labelFont.render(string, True, config.WHITE)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx + x
    textRect.centery = windowSurface.get_rect().centery + y
    windowSurface.blit(text, textRect)
    
# Set up the window. set up the window for the screen.
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
pygame.mouse.set_visible(0)
windowSurface = pygame.display.set_mode(config.RESOLUTION)    

speedo_files = ['finaldeg_%i.png' % i for i in range(0, 96, 5)]
speedom = [pygame.image.load("speedometer\\"+file) for file in speedo_files]
#print(speedom)

#warning_files = ['symbol_%i.png' % i for i in range(1,20)]
#warnings = [pygame.image.load("symbols\\"+file) for file in speedo_files]
# Set up fonts
readoutFont = pygame.font.SysFont("Arial.ttf",40)
labelFont = pygame.font.SysFont("Arial.ttf",15)


# Load the eter gauge image.
'''img = pygame.image.load("/home/pi/images/m3_logo.png")
img_button = img.get_rect(topleft=(135, 220))'''

# Set the caption.
pygame.display.set_caption('CAR PI')

clock = pygame.time.Clock()

    # Read the log file into memory.
dashboard_data = log.readLog('logs\debug_log.csv')
    # Get the length of the log.
logLength = len(dashboard_data)

# Run the game loop
while True:    
    windowSurface.fill(config.BLACK)  
    speedocoords = (windowSurface.get_rect().centerx-50,\
              windowSurface.get_rect().centery-120)
    # Load the speedo image
    windowSurface.blit(speedom[log.speedo_iter], speedocoords)
    #print(log.speedo_iter)
    #print(log.intakeTemp)
        # Draw the intake temp readout and label.
    #drawText(str(ecu.intakeTemp) + "\xb0C", 190, 105, "readout")
    #drawText("Intake", 190, 140, "label")
    tempcoords = (windowSurface.get_rect().centerx-110,\
              windowSurface.get_rect().centery - 25)    
    if int(log.intakeTemp) < 100:
        windowSurface.blit(pygame.image.load("symbols\\Water_Level_Grey.png"), tempcoords)
    else:
        windowSurface.blit(pygame.image.load("symbols\\Water_Level_Red.png"), tempcoords)
    
    battcoords = (windowSurface.get_rect().centerx-165,\
              windowSurface.get_rect().centery - 130)
    if int(log.batt_level) == 0:
        windowSurface.blit(pygame.image.load("symbols\\Batt_dead.png"), battcoords)    
    elif int(log.batt_level) < 33:
        windowSurface.blit(pygame.image.load("symbols\\Batt_1third.png"), battcoords)
    elif int(log.batt_level) < 67:
        windowSurface.blit(pygame.image.load("symbols\\Batt_2thirds.png"), battcoords)
    else:
        windowSurface.blit(pygame.image.load("symbols\\Batt_full.png"), battcoords)
        
    sensorcoords = (windowSurface.get_rect().centerx-175,\
              windowSurface.get_rect().centery - 25)
    if int(log.sensor) == 0:
        windowSurface.blit(pygame.image.load("symbols\\Sensor_grey.png"), sensorcoords)
    elif int(log.sensor) == 1:
        windowSurface.blit(pygame.image.load("symbols\\Sensor_yellow.png"), sensorcoords)
    else:
        windowSurface.blit(pygame.image.load("symbols\\Sensor_red.png"), sensorcoords)
    
    pedalcoords = (windowSurface.get_rect().centerx-215,\
              windowSurface.get_rect().centery - 25)
    if int(log.pedal) == 0:
        windowSurface.blit(pygame.image.load("symbols\\Pedal_grey.png"), pedalcoords)
    else:
        windowSurface.blit(pygame.image.load("symbols\\Pedal_red.png"), pedalcoords)
        
    battvcoords = (windowSurface.get_rect().centerx-225,\
              windowSurface.get_rect().centery + 25)
    if int(log.pedal) == 0:
        windowSurface.blit(pygame.image.load("symbols\\Batt_1v_grey.png"), battvcoords)
    else:
        windowSurface.blit(pygame.image.load("symbols\\Batt_12v_red.png"), battvcoords)
        
    cancoords = (windowSurface.get_rect().centerx-170,\
              windowSurface.get_rect().centery + 25)
    if int(log.sensor) == 0:
        windowSurface.blit(pygame.image.load("symbols\\CAN_grey.png"), cancoords)
    elif int(log.sensor) == 1:
        windowSurface.blit(pygame.image.load("symbols\\CAN_yellow.png"), cancoords)
    else:
        windowSurface.blit(pygame.image.load("symbols\\CAN_red.png"), cancoords)
        
    voltagecoords = (windowSurface.get_rect().centerx-170,\
              windowSurface.get_rect().centery + 70)
    if int(log.sensor) == 0:
        windowSurface.blit(pygame.image.load("symbols\\Voltage_Grey.png"), voltagecoords)
    elif int(log.sensor) == 1:
        windowSurface.blit(pygame.image.load("symbols\\Voltage_Yellow.png"), voltagecoords)
    else:
        windowSurface.blit(pygame.image.load("symbols\\Voltage_red.png"), voltagecoords)

    
        # Draw the coolant temp readout and label.
    #drawText(str(ecu.coolantTemp) + "\xb0C", -160, 105, "readout")
    #drawText("Coolant", -170, 140, "label")
        # Draw the speed readout and label.
    drawText(str(log.speed) + " kph", 95, 0, "readout")
    drawText(str(log.intakeTemp), -88, -88, "readout")
    drawText(str(log.batt_temp), -200, -88, "readout")
    drawText("INTAKE", -88, -115, "label")
    drawText("TEMP", -88, -65, "label")
    drawText("BATT", -200, -115, "label")
    drawText("TEMP", -200, -65, "label")
    
    
    #drawText("Speed", 180, 50, "label")
    #print(log.speed)
        # Draw the throttle position readout and label.
    '''drawText(str(ecu.throttlePosition) + " %", 190, -145, "readout")
    drawText("Throttle", 190, -110, "label")
        # Draw the engine load readout and label.
    drawText(str(ecu.engineLoad) + " %", 0, -145, "readout")
    drawText("Load", 0, -110, "label")'''
        
        # If debug flag is set, feed fake data so we can test the GUI.
    if config.debugFlag:      
        #Debug gui display refresh 10 times a second.
        if config.gui_test_time > 20:
            log.getLogValues(dashboard_data)
            config.gui_test_time = 0

    # Update the clock.
    dt = clock.tick(5)
    
    config.time_elapsed_since_last_action += dt
    config.gui_test_time += dt
   
    # draw the window onto the screen
    pygame.display.update()
