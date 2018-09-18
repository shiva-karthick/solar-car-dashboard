try:
    import pygame
    import math
    import time
    import random
    import pygame.camera
    from pygame.locals import *
except ImportError as err:
    print("Check your imports !")
    print(str(err))


class Initialise(object):
    # Colour definitions (Red ,Green, Blue)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    BROWN = (83, 91, 36)
    SILVER = (192, 192, 192)

    pygame.init()
    pygame.camera.init()
    pygame.display.set_caption("Camera in pygame")
    clock = pygame.time.Clock()
    resolution = (1024, 600)
    screen = pygame.display.set_mode(resolution)


class Camera(Initialise):
    camList = pygame.camera.list_cameras()
    if camList:
        cam = pygame.camera.Camera(camList[0],(640,480))
    else:
        raise ValueError("Sorry no cameras are detected !")
    
    def open_camera(self):
##        cam = pygame.camera.Camera()
        Camera.cam.start()

    def close_camera(self):
        Camera.cam.stop()    

if __name__ == "__main__":
    initialise = Initialise()
    camera = Camera()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                camera.open_camera()
            elif event.key == pygame.K_v:
                camera.close_camera()

    initialise.clock.tick(60)
    pygame.display.update()
