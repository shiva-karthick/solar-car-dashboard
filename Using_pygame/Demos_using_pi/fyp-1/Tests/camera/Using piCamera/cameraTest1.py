try:
    import pygame
    import math
    import time
    import random
    import picamera
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
    pygame.display.set_caption("Dashboard")
    clock = pygame.time.Clock()
    resolution = (1024, 600)
    screen = pygame.display.set_mode(resolution)


class CameraTest(object):
    def UseCamera(self):
        camera = picamera.PiCamera()
        camera.preview_fullscreen = False
        camera.preview_window = (0, 300, 1024, 300)
        camera.resolution = (1024, 300)
        camera.start_preview()


if __name__ == "__main__":
    initialise = Initialise()
    camera = CameraTest()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    initialise.clock.tick(30)
    pygame.display.update()
