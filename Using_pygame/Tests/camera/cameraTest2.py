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
    cameraPos = (0, 300, 1024, 300)
    cameraBlock = pygame.Surface((1024, 300))

    def UseCamera(self):
        camera = picamera.PiCamera()
        camera.preview_fullscreen = False
        camera.preview_window = (0, 300, 1024, 300)
        camera.resolution = (1024, 300)
        camera.start_preview()

        Initialise.screen.blit(
            Camera.cameraBlock, (Camera.cameraPos[0], Camera.cameraPos[1]))


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
                camera.UseCamera()
            else:
                camera.stop_preview()

    initialise.clock.tick(60)
    pygame.display.update()
