try:
    import pygame
    import sys
    import math
    import time
    import serial
    import RPi.GPIO as GPIO
    import picamera
except Exception as err:
    print(str(err))
    pass

pygame.init()
clock = pygame.time.Clock()
ser = serial.Serial('/dev/ttyACM0',9600)  #'/dev/ttyACM0' for raspberry pi
ser = "DATA, TIME, 0, 29.0,30,45.100,103.2935"
pygame.display.set_caption("Dashboard")

resolution  = (1024,600)
speedPos    = (175,0,674,270)
tempPos     = (0,45,175,270)
batPos      = (849,45,175,270)
cameraPos   = (0,300,1024,300)
taskbarPos  = (0,265,1024,35)

screen = pygame.display.set_mode(resolution)
speedMeter  = pygame.Surface((speedPos[2],speedPos[3]))
tempMeter   = pygame.Surface((tempPos[2],tempPos[3]))
batMeter    = pygame.Surface((batPos[2],batPos[3]))
cameraBlock = pygame.Surface((cameraPos[2],cameraPos[3]))
taskbar     = pygame.Surface((taskbarPos[2],taskbarPos[3]))
surfaces = (screen,speedMeter,tempMeter,batMeter,cameraBlock,taskbar)

tempimage = pygame.image.load("temp.png").convert()
battimage = pygame.image.load("batt.png").convert()
tempimage = pygame.transform.scale(tempimage,(80,50))
battimage = pygame.transform.scale(battimage,(60,40))
tempimage.set_colorkey((0,0,0))
battimage.set_colorkey((255,255,255))

BLACK   = (0  ,0  ,0  )
GREY    = (28 ,40 ,51 )
WHITE   = (255,255,255)
YELLOW  = (255,255,0  )
RED     = (255,0  ,0  )
GREEN   = (0  ,255,0  )
BLUE    = (0  ,191,255)
ORANGE  = (255,128,0  ) 

pi      = math.pi
gps     = 0
speed   = 1
batt    = 1
temp    = 1
motor   = 0

updateCount = 0
def UpdateValues():
    global updateCount
    if (updateCount <= 3):
        str1 = str(ser.readline())
        updateCount += 1
    else:
        values = str1.split(',')
        global gps, speed, batt, temp, motor
        gps     = int(values[5])
        speed   = int(values[3])
        batt    = int(values[13])
        temp    = int(values[10])
        motor   = float(values[15],3)


def UseCamera():
        camera = picamera.PiCamera()
        camera.preview_fullscreen = False
        camera.preview_window = (0,300,1024,300)
        camera.resolution = (1024,300)
        camera.start_preview()

def Font(fonttype,size):
    fontsize = pygame.font.SysFont(fonttype,size)
    return(fontsize)

def Meter(
        typeOfMeter=None,
        destination=None,
        color=None,
        posX=0,
        posY=0,
        diameter=0,
        angle=0,
        division=0,
        thickness=0,
        value=0
    ):
    degreesDifference = angle / division

    if typeOfMeter == "TEMP": #tempsensor
        pygame.draw.arc(destination,WHITE,[(posX+10)+thickness,(posY+10)+thickness,(diameter-20-thickness*2),(diameter-20)-thickness*2],7*pi/4,13*pi/8,3)
        pygame.draw.arc(destination,color,[posX+10,posY+10,diameter-20,diameter-20],3*pi/2+(-value)*degreesDifference,7*pi/4,thickness)
        blocker  = destination.subsurface(diameter/2,diameter/2,diameter/2,diameter/2)
        labelBox = destination.subsurface(diameter/3.4,diameter/3.4,diameter/2.5,diameter/2.5)
        blocker.fill(GREY)
        labelBox.fill(GREY)
        labelValue = Font("Digital-7",62).render(str(temp),1,YELLOW)
        labelTitle = Font("Digital-7",18).render(typeOfMeter,1,WHITE)
        labelUnit  = Font("Digital-7",38).render("'C",1,WHITE)
        labelValuePos = labelValue.get_rect()
        labelTitlePos = labelTitle.get_rect()
        labelUnitPos  = labelUnit.get_rect()
        labelValuePos.center = ((diameter/2.5)/2,(diameter/2.5)/1.9)
        labelTitlePos.center = ((diameter/2),(diameter/3.5))
        labelUnitPos.center  = ((diameter/2)/1.8,(diameter/2)/3.5)
        labelBox.blit(labelValue,labelValuePos)
        destination.blit(labelTitle,labelTitlePos)
        blocker.blit(labelUnit,labelUnitPos)

    elif typeOfMeter == "BATT": #batterymeter
        pygame.draw.arc(destination,WHITE,[(posX+10)+thickness,(posY+10)+thickness,(diameter-20-thickness*2),(diameter-20)-thickness*2],11*pi/8,5*pi/4,3)
        pygame.draw.arc(destination,color,[posX+10,posY+10,diameter-20,diameter-20],5*pi/4,3*pi/2+(value)*degreesDifference,thickness)
        blocker  = destination.subsurface(0,diameter/2,diameter/2,diameter/2)
        labelBox = destination.subsurface(diameter/3.4,diameter/3.4,diameter/2.5,diameter/2.5)
        blocker.fill(GREY)
        labelBox.fill(GREY)
        labelValue = Font("Digital-7",62).render(str(temp),1,GREEN)
        labelTitle = Font("Digital-7",18).render(typeOfMeter,1,WHITE)
        labelUnit  = Font("Digital-7",38).render("%",1,WHITE)
        labelValuePos = labelValue.get_rect()
        labelTitlePos = labelTitle.get_rect()
        labelUnitPos  = labelUnit.get_rect()
        labelValuePos.center = ((diameter/2.5)/2,(diameter/2.5)/1.9)
        labelTitlePos.center = ((diameter/2),(diameter/3.5))
        labelUnitPos.center  = ((diameter/2)/2.2,(diameter/2)/3.5)
        labelBox.blit(labelValue,labelValuePos)
        destination.blit(labelTitle,labelTitlePos)
        blocker.blit(labelUnit,labelUnitPos)

    elif typeOfMeter == "SPEED": #speedometer
        pygame.draw.arc(destination,WHITE,[(posX+10)+thickness,(posY+5)+thickness,(diameter-20)-thickness*2,((speedPos[3]*2)-20)-thickness*2],7*pi/4,5*pi/4,3)
        pygame.draw.arc(destination,color,[posX+10,posY+5,diameter-20,(speedPos[3]*2)-20],pi+(-value)*degreesDifference,5*pi/4,thickness)
        labelBox = destination.subsurface((diameter/2)/2,speedPos[3]/3.5,diameter/2,speedPos[3]/1.4)
        labelBox.fill(GREY)
        labelBox.set_alpha(0)
        labelValue = Font("Digital-7",200).render(str(value),1,BLUE)
        labelTitle = Font("Digital-7",36).render(typeOfMeter,1,WHITE)
        labelUnit  = Font("Digital-7",36).render("km/h",1,WHITE)
        labelValuePos = labelValue.get_rect()
        labelTitlePos = labelTitle.get_rect()
        labelUnitPos  = labelUnit.get_rect()
        labelValuePos.center = ((diameter/2)/2,(speedPos[3]/1.4)/2)
        labelTitlePos.center = ((diameter/2),(speedPos[3]/3.5))
        labelUnitPos.center  = ((diameter/1.35),(speedPos[3]/1.2))
        labelBox.blit(labelValue,labelValuePos)
        destination.blit(labelTitle,labelTitlePos)
        destination.blit(labelUnit,labelUnitPos)

def Taskbar(
        title=None,
        posX=0,
        posY=0,
        width=0,
        height=0,
        value=0
    ):
    if title == "GPS": #shows whether gps is connected
        bar = taskbar.subsurface(posX,posY,width,height)
        label = pygame.draw.rect(bar,WHITE,(0,posY-5,width,height),5)
        GPS = Font("Digital-7",24).render("GPS:",1,WHITE)
        if gps != 1:    gpsText = Font("Digital-7",24).render("Disconnected",1,RED)
        else:           gpsText = Font("Digital-7",24).render("Connected",1,GREEN)
        GPSBox = GPS.get_rect()
        gpsBox = gpsText.get_rect()
        GPSBox.center = (width/2-60,height/2)
        gpsBox.center = (width/2+20,height/2)
        bar.blit(GPS,GPSBox)
        bar.blit(gpsText,gpsBox)

    elif title == "MOTOR": #speed
        bar = taskbar.subsurface(posX,posY,width,height)
        label = pygame.draw.rect(bar,WHITE,(0,posY-5,width,height),5)
        motorBar = pygame.draw.rect(bar,(255,180-value*3,0),(3,posY-2,(width-6)*(value/60),height-6))
        motorText = Font("Digital-7",24).render(str(motor),1,WHITE)
        motorBox  = motorText.get_rect()
        motorBox.center = (width/2+225,height/2)
        bar.blit(motorText,motorBox)
                     
    elif title == "TIME": #time
        bar = taskbar.subsurface(posX,posY,width,height)
        label = pygame.draw.rect(bar,WHITE,(0,posY-5,width,height),5)
        TIME = Font("Digital-7",24).render(time.ctime(),1,WHITE)
        timeBox = TIME.get_rect()
        timeBox.center = (width/2,height/2)
        bar.blit(TIME,timeBox)

state = True
fullScreen = True
while True:
    try: 
        for event in pygame.event.get(): #keybind for quiting
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: #keybind for fullscreen
                if event.key == pygame.K_f:
                    if fullScreen != False:
                        screen = pygame.display.set_mode((resolution),pygame.FULLSCREEN)
                        screen.fill(BLACK)
                        fullScreen = False
                    else:
                        screen = pygame.display.set_mode((resolution))
                        screen.fill(BLACK)
                        fullScreen = True
            if event.type == pygame.KEYDOWN: #keybind for camera
                if event.key == pygame.K_c:
                    if state != False:
                        UseCamera()
                        state = False
                    else:
                        camera.stop_preview()
                        state = True
            
        for surface in surfaces:
            surface.fill(GREY)
        
        Meter("TEMP",tempMeter,YELLOW,0,0,tempPos[2],3*pi/2,100,15,temp)
        Meter("BATT",batMeter,GREEN,0,0,batPos[2],3*pi/2,100,15,batt)
        Meter("SPEED",speedMeter,BLUE,0,0,speedPos[2],pi,100,25,speed)

        Taskbar("GPS",0,5,244,30)
        Taskbar("MOTOR",244,5,536,30,motor)
        Taskbar("TIME",780,5,244,30)

        tempMeter.blit(tempimage,(80,130))
        batMeter.blit(battimage,(20,140))

        screen.blit(speedMeter,(speedPos[0],speedPos[1]))
        screen.blit(tempMeter,(tempPos[0],tempPos[1]))
        screen.blit(batMeter,(batPos[0],batPos[1]))
        screen.blit(cameraBlock,(cameraPos[0],cameraPos[1]))
        screen.blit(taskbar,(taskbarPos[0],taskbarPos[1]))

'''     #causes value to loop
        if speed < 100:   speed+=1
        else:             speed=1
        if temp < 100:    temp+=1
        else:             temp=1
        if batt < 100:    batt+=1
        else:             batt=1
        if motor < 60:    motor+=1
        else:             motor=0
'''

        #causes the symbol to show up
        if temp > 50:  tempimage.set_alpha(255)
        else:          tempimage.set_alpha(50)
        if batt < 35:  battimage.set_alpha(255)
        else:          battimage.set_alpha(50)

        UpdateValues()
        clock.tick(50)
        pygame.display.update()
        
    except Exception as err:
        print(str(err))
