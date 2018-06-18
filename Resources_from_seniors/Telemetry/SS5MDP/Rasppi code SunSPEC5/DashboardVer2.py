#!/usr/bin/python

### library ###
import pygame
import math
import time
import sys
#import serial
#import RPi.GPIO as GPIO
#import picamera

### initialization ###
pygame.init()
pygame.display.set_caption("Dashboard")
#ser = serial.Serial('COM16',9600) #  '/dev/ttyACM0' for raspberry pi

#camera = picamera.PiCamera()
resolution= (1024,600)
screen = pygame.display.set_mode((1024,600))
surfaceSpeed   = pygame.Surface((674,375))
surfaceBat     = pygame.Surface((175,375))
surfaceTemp    = pygame.Surface((175,375))
surfaceSymL    = pygame.Surface((100,100))
surfaceSymR    = pygame.Surface((115,90))
surfaceCamera  = pygame.Surface((1024,250))
surfaceTaskbar = pygame.Surface((1024,35))

### symbols ###
tempimage = pygame.image.load("temp.png").convert()
battimage = pygame.image.load("batt.png").convert()
tempimage.set_colorkey((0,0,0))
battimage.set_colorkey((255,255,255))
tempimage.set_alpha(50)
battimage.set_alpha(50)

### variables ###
BLACK = (28,40,51)
WHITE = (255,255,255)
YELLOW = (255,255,0)
RED = (255,0,0)
pi = math.pi
speed = 1
temp = 1
bat = 1

def Gauge(
        meterDestination,
        positionX=0,
        positionY=0,
        color=0,
        diameter=0,
        division=0,
        startAngle=0,
        endAngle=0,
        angleRatio=False,
        value=0,
        width=0,
        blocker=False,
        batt_label = False,
        speed_label = False
        
    ):

    destination = meterDestination
    position = (positionX,positionY)
    color = color
    diameter = diameter
    degreesDifference = startAngle/division
    startAngle = startAngle
    endAngle = endAngle
    value = value
    width = width
    fontSize = pygame.font.SysFont("", 0)
    backgroundColour = (28,40,51)
    
    if blocker == True:
        surfaceBlock = pygame.Surface((diameter,diameter/2))
        surfaceBlock.fill(BLACK)
    else:
        pass
        
    
    if angleRatio == True:
        #ratio at left
        pygame.draw.arc(surfaceBlock,color,[0,0,diameter,diameter],
                        startAngle+value*degreesDifference,endAngle,width)
        destination.blit(surfaceBlock,(position[0],position[1]))
        pygame.draw.arc(surfaceBlock,color,[0,0,diameter,diameter],endAngle,startAngle,3)
        destination.blit(surfaceBlock,(position[0],position[1]))
    else:
        pygame.draw.arc(destination,color,[position[0],position[1],diameter,diameter],
                        startAngle,endAngle+value*degreesDifference,width)
        pygame.draw.arc(destination,color,[position[0],position[1],diameter,diameter],
                       startAngle,endAngle+3*pi/2,3)
   
    if batt_label:
        Label = ( font("Digital-7", 77).render(batt_label[0],1,YELLOW),
                      font("Digital-7", 64).render(batt_label[1],1,YELLOW),
                      font("Digital-7", 50).render(batt_label[2],1,YELLOW) )
        Value = Label[0].get_rect()
        Type = Label[1].get_rect()
        Unit = Label[2].get_rect()
        Value.center = position[0]+(resolution[0]*0.15625*0.48),position[1]+(resolution[0]*0.15625/2)
        Type.center = position[0]+(resolution[0]*0.15625*0.5),position[1]-(resolution[0]*0.05)
        Unit.center = position[0]+(resolution[0]*0.15625*0.3),position[1]+(resolution[0]*0.15625*0.9)
        destination.blit(Label[0], (Value))
        destination.blit(Label[1], (Type))
        destination.blit(Label[2], (Unit))

    if speed_label:
        Label = ( font("Digital-7", int(resolution[0]*0.1875)).render(speed_label[0], 1, YELLOW, ),
                      font("Digital-7", int(resolution[0]*0.0625)).render(speed_label[1], 1, YELLOW, ),
                      font("Digital-7", int(resolution[0]*0.0625)).render(speed_label[2], 1, YELLOW, ) )
        Value = Label[0].get_rect()
        Type = Label[1].get_rect()
        Unit = Label[2].get_rect()
        Value.center = 15+(250),position[1]+(resolution[0]*0.5625*0.35)
        Type.center = 15+(450),position[1]+(resolution[0]*0.5625*0.28)
        Unit.center = 15+(450),position[1]+(resolution[0]*0.5625*0.43)
        destination.blit(Label[0], (Value))
        destination.blit(Label[1], (Type))
        destination.blit(Label[2], (Unit))
        
    return(position)

def UseCamera():
        camera.preview_fullscreen = False
        camera.preview_window = (0,360,1024,250)
        camera.resolution = (1024,250)
        camera.start_preview()

def font(fonttype,size):
    fontsize=pygame.font.SysFont(fonttype,size)
    return(fontsize)

def update_label():
    str1=ser.readline()
    str2= str(str1)
    if len(str2.split(',')) > 4 :
        a,b,c,d,e= str2.split(',')
        global speed,bat,temp
        speed = int(b)
        bat= int(c)
        temp= int(d)
    

### main loop ###
screen.fill(BLACK)
state = True
fullScreen = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_c:
                if state != False:
                    UseCamera()
                    state = False
                else:
                    camera.stop_preview()
                    state = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if fullScreen != False:
                    screen = pygame.display.set_mode((resolution),pygame.FULLSCREEN)
                    screen.fill(BLACK)
                    fullScreen = False
                else:
                    screen = pygame.display.set_mode((resolution))
                    screen.fill(BLACK)
                    fullScreen = True 
            
    surfaceSpeed.fill(BLACK)
    surfaceBat.fill(BLACK)
    surfaceTemp.fill(BLACK)
    surfaceSymL.fill(BLACK)
    surfaceSymR.fill(BLACK)
    surfaceTaskbar.fill(BLACK)
    surfaceSymL.blit(tempimage,(0,0))
    surfaceSymR.blit(battimage,(0,0))

    '''
    meterDestination,positionX=0,positionY=0,color=0,diameter=0,division=0,
    startAngle=0,endAngle=0,angleRatio=False,value=0,width=0,blocker=False,
    batt_label=False,speed_label=False
    '''
    Gauge(surfaceSpeed,55,10,WHITE,575,130,
          pi,3*pi/2,True,-speed,30,True,
          False,(str(speed),"Spd","km/h"))
    Gauge(surfaceTemp,5,130,WHITE,(resolution[0]*0.15625),100,
          3*pi/2,3*pi/2,False,temp,15,False,
          (str(temp),"Temp","'C"))
    Gauge(surfaceBat,10,130,WHITE,(resolution[0]*0.15625),100,
          3*pi/2,3*pi/2,False,bat,15,False,
          (str(bat),"Batt","%"))

    taskbar = pygame.draw.rect(surfaceTaskbar,WHITE,(0,0,1024,35),5)
    timeLabel = pygame.draw.rect(surfaceTaskbar,WHITE,taskbar.inflate(-600,0),3)
    time = font("Digital-7",14).render("Sat, 08:00:00",True,YELLOW)
    #Time = timeLabel(time)
    
    
    screen.blit(surfaceSpeed,(175,0))
    screen.blit(surfaceBat,(849,0))
    screen.blit(surfaceTemp,(0,0))
    screen.blit(surfaceSymL,(150,25))
    screen.blit(surfaceSymR,(750,30))
    screen.blit(surfaceCamera,(0,345))
    screen.blit(surfaceTaskbar,(0,310))

    if speed < 130:
        speed += 1
    else:
        speed = 1

    if temp < 100:
        temp += 1
        if temp > 50:
            tempimage.set_alpha(255)
    else:
        temp=1
        tempimage.set_alpha(50)
        
    if bat < 100:
        bat += 1
        if bat > 50:
            battimage.set_alpha(255)
    else:
        bat = 1
        battimage.set_alpha(50)
    
    #update_label()
    pygame.display.update()
    
