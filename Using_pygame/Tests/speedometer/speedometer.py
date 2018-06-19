try:
    import pygame
    import math
    import time
    import random
except ImportError as err:
    print("Check your imports !")
    print(str(err))


class Speedometer(object):
    # Colour definitions (Red ,Green, Blue)
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
        pygame.display.set_caption("Dashboard")
        self.clock = pygame.time.Clock()
        self.resolution = (1024, 600)
        self.screen = pygame.display.set_mode(self.resolution)
        self.PI = math.pi

    def load_image(self):
        self.speedometer_image = pygame.image.load("speed.png")
        self.screen.blit(self.speedometer_image, (100, 5))

    def draw_arc(self):
        # pygame.draw.arc()

        # Good example arc below ->
        # pygame.draw.arc(self.screen, Speedometer.YELLOW,
        #                 (235, 75, 525, 525), math.radians(-42), math.radians(223), 4)

        # draw a partial section of an ellipse
        # arc(Surface, color, Rect, start_angle, stop_angle, width=1) -> Rect
        """Draws an elliptical arc on the Surface. The rect argument is the area that the ellipse will fill. The two angle arguments are the initial and final angle in radians, with the zero on the right. The width argument is the thickness to draw the outer edge.

        TAKE NOTE: <Worth mentioning> the initial angle must be less than the final angle; otherwise it will draw the full elipse."""
        pygame.draw.arc(self.screen, Speedometer.YELLOW,
                        (235, 75, 525, 525), math.radians(-42), math.radians(223), 4)


if __name__ == "__main__":
    speedometer = Speedometer()
    while True:
        # This is your event handling loop and you might have a logic loop.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        speedometer.load_image()
        speedometer.draw_arc()
        pygame.display.update()
        speedometer.clock.tick(60)
