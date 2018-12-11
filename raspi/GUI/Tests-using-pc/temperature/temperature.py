try:
    import pygame
    import math
    import time
    import random
except ImportError as err:
    print("Check your imports !")
    print(str(err))


class Temperature(object):
    # Colour definitions (Red ,Green, Blue)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    BROWN = (83, 91, 36)
    LIGHT_BLUE = (66, 220, 244)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Dashboard")
        self.clock = pygame.time.Clock()
        self.resolution = (1024, 600)
        self.screen = pygame.display.set_mode(self.resolution)
        self.a = 180

    def draw_arc(self):
        # pygame.draw.arc()

        # Good example arc below ->
        # pygame.draw.arc(self.screen, Temperature.YELLOW,
        #                 (235, 75, 525, 525), math.radians(-42), math.radians(223), 4)

        # draw a partial section of an ellipse
        # arc(Surface, color, Rect, start_angle, stop_angle, width=1) -> Rect
        """Draws an elliptical arc on the Surface. The rect argument is the area that the ellipse will fill. The two angle arguments are the initial and final angle in radians, with the zero on the right. The width argument is the thickness to draw the outer edge.

        TAKE NOTE: <Worth mentioning> the initial angle must be less than the final angle; otherwise it will draw the full elipse."""
        pygame.draw.arc(self.screen, Temperature.YELLOW,
                        (50, 75, 200, 200), math.radians(self.a), math.radians(-180), 25)
        if self.a != 0:
            self.a -= 1


class Text(Temperature):
    # def text_objects(text, font):
    #     textSurface = font.render(text, True, RED)
    #     return textSurface, textSurface.get_rect()

    def message_display(self, text):
        largeText = pygame.font.Font("freesansbold.ttf", 20)
        # The text is inside a rectangle and can be referenced by a rectangle.
        textSurface = largeText.render(text, True, self.LIGHT_BLUE)

        # TextSurface, TextRect = text_objects(text, largeText)
        TextRect = textSurface.get_rect()
        TextRect.center = (150, 150)
        self.screen.blit(textSurface, TextRect)


if __name__ == "__main__":
    temperature = Temperature()
    text = Text()
    while True:
        # This is your event handling loop and you might have a logic loop.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        temperature.draw_arc()
        text.message_display(text="{} degrees".format(10))
        pygame.display.update()
        temperature.clock.tick(60)
