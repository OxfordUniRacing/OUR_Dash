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

background_files = ['finaldeg_%i.png' % i for i in range(0, 96, 5)]
ground = [pygame.image.load("speedometer\\"+file) for file in background_files]
print(ground)
# Set up fonts
readoutFont = pygame.font.SysFont("Arial.ttf",40)
labelFont = pygame.font.SysFont("Arial.ttf",30)

# Load the speedometer gauge image.
'''img = pygame.image.load("/home/pi/images/m3_logo.png")
img_button = img.get_rect(topleft=(135, 220))'''

# Set the caption.
pygame.display.set_caption('CAR PI')

clock = pygame.time.Clock()

    # Read the log file into memory.
dashboard_data = log.readLog('logs\debug_log.csv')
    # Get the length of the log.
logLength = len(dashboard_data)

print(dashboard_data[0][0])

# Run the game loop
while True:    
    windowSurface.fill(config.BLACK)  
    coords = (windowSurface.get_rect().centerx-50,\
              windowSurface.get_rect().centery-120)
    # Load the speedo image
    windowSurface.blit(ground[log.speedo_iter], coords)
    print(log.speedo_iter)
        # Draw the intake temp readout and label.
    #drawText(str(ecu.intakeTemp) + "\xb0C", 190, 105, "readout")
    #drawText("Intake", 190, 140, "label")

        # Draw the coolant temp readout and label.
    #drawText(str(ecu.coolantTemp) + "\xb0C", -160, 105, "readout")
    #drawText("Coolant", -170, 140, "label")
        # Draw the speed readout and label.
    drawText(str(log.speed) + " kph", 95, 0, "readout")
    #drawText("Speed", 180, 50, "label")
    print(log.speed)
        # Draw the throttle position readout and label.
    '''drawText(str(ecu.throttlePosition) + " %", 190, -145, "readout")
    drawText("Throttle", 190, -110, "label")
        # Draw the engine load readout and label.
    drawText(str(ecu.engineLoad) + " %", 0, -145, "readout")
    drawText("Load", 0, -110, "label")'''
        
        # If debug flag is set, feed fake data so we can test the GUI.
    if config.debugFlag:      
        #Debug gui display refresh 10 times a second.
        if config.gui_test_time > 100:
            log.getLogValues(dashboard_data)
            config.gui_test_time = 0

    # Update the clock.
    dt = clock.tick(5)
    
    config.time_elapsed_since_last_action += dt
    config.gui_test_time += dt
   
    # draw the window onto the screen
    pygame.display.update()
