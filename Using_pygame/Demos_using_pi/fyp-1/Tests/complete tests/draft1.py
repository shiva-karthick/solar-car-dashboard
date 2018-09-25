try:
    import pygame
    import math
    import time
    import random
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

    def __init__(self):
        # pygame.init()
        # pygame.display.set_caption("Dashboard")
        self.clock = pygame.time.Clock()
        self.resolution = (1024, 600)
        self.screen = pygame.display.set_mode(self.resolution)


class Battery(Initialise):
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

    def __init__(self):
        super().__init__()
        self.x = 145

    def draw_rect(self):
        pygame.draw.rect(self.screen, Battery.SILVER, (950, 60, 15, 30))
        pygame.draw.rect(self.screen, Battery.WHITE, (800, 25, 150, 100), 3)
        # pygame.draw.rect(self.screen, Battery.GREEN, (802, 27, 145, 97))
        # if self.x != 145:
        #     pygame.draw.rect(self.screen, Battery.GREEN, (802, 27, self.x, 97))
        #     self.x += 1
        pygame.draw.rect(self.screen, Battery.GREEN, (802, 27, self.x, 97))


class Speedometer(Initialise):
    # Colour definitions (Red ,Green, Blue)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    BROWN = (83, 91, 36)
    ORANGE = (250, 167, 41)

    def __init__(self):
        super().__init__()
        self.PI = math.pi
        self.a = 200

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
                        (235, 75, 525, 525), math.radians(self.a), math.radians(223), 5)
        if self.a != -42:
            self.a -= 1


class Text(Battery):
    def message_display(self, text, x_position, y_position):
        largeText = pygame.font.Font("freesansbold.ttf", 20)
        # The text is inside a rectangle and can be referenced by a rectangle.
        textSurface = largeText.render(text, True, self.CYAN)

        # TextSurface, TextRect = text_objects(text, largeText)
        TextRect = textSurface.get_rect()
        TextRect.center = (x_position, y_position)
        self.screen.blit(textSurface, TextRect)


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Dashboard")

    initialise = Initialise()
    battery = Battery()
    text = Text()
    speedometer = Speedometer()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        speedometer.load_image()
        speedometer.draw_arc()
        battery.draw_rect()

        text.message_display(text="{} %".format(
            100), x_position=865, y_position=150)
        text.message_display(text="{}".format(
            75), x_position=500, y_position=340)

        initialise.clock.tick(60)
        pygame.display.update()
