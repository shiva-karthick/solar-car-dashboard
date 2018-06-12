import pygame
from pygame.locals import *


class Test_Camera(object):

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    BROWN = (83, 91, 36)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Solar-Car Dashboard")

        self.display_width = 1024
        self.display_height = 600
        self.screen = pygame.display.set_mode(
            (self.display_width, self.display_height))

        self.clock = pygame.time.Clock()
        self.clock.tick(60)

    def colours(self):
        # Colour definitions (Red ,Green, Blue)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)
        self.CYAN = (0, 255, 255)
        self.BROWN = (83, 91, 36)

    def load_speedometer(self):
        self.speedometer_image = pygame.image.load(
            "C:\\programming\\python\programs\\solar-car-dashboard\\Using_pygame\\all_tests\\speedometer.jpg")
        self.speedometer_image = pygame.transform.scale(
            self.speedometer_image, (500, 500))
        self.screen.blit(self.speedometer_image, (100, 100))
        # pygame.display.update()


if __name__ == "__main__":
    # Initilise all pygame modules
    # pygame.init()

    test_camera = Test_Camera()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # print(event)

        # test_camera.screen.fill(test_camera.BROWN)
        test_camera.load_speedometer()
        # pygame.camera.list_cameras()
        pygame.display.update()
