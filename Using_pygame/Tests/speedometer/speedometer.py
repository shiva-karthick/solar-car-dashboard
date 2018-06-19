try:
    import pygame
    import math
    import time
    import random
except ImportError as err:
    print("Check your imports !")
    print(str(err))


class Speedometer(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Dashboard")
        self.clock = pygame.time.Clock()
        self.resolution = (1024, 600)
        self.screen = pygame.display.set_mode(self.resolution)
