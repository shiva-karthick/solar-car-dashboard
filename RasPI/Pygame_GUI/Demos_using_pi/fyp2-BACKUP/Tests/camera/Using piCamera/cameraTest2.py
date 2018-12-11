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
    pygame.display.set_caption("Camera !")
    clock = pygame.time.Clock()
    resolution = (1024, 600)
    screen = pygame.display.set_mode(resolution)


class Camera(Initialise):
    # The below are declared as class variables
    camera_position = (0, 300, 1024, 300)
    camera_block = pygame.Surface((1024, 300))

    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.preview_fullscreen = False
        self.camera.preview_window = (0, 300, 1024, 300)
        self.camera.resolution = (1024, 300)

    def use_camera(self):
        self.camera.start_preview()
        Initialise.screen.blit(
            Camera.camera_block, (Camera.camera_position[0], Camera.camera_position[1]))

    def  stop_camera(self):
        self.camera.stop_preview()

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
                camera.use_camera()
            elif event.key == pygame.K_v:
                camera.stop_camera()

    initialise.clock.tick(60)
    pygame.display.update()
