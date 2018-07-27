try:
    import pygame
    import math
    import time
    import random
except ImportError as err:
    print("Check your imports !")
    print(str(err))


class Battery(object):
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
        pygame.init()
        pygame.display.set_caption("Dashboard")
        self.clock = pygame.time.Clock()
        self.resolution = (1024, 600)
        self.screen = pygame.display.set_mode(self.resolution)
        self.x = 0

    def draw_rect(self):
        pygame.draw.rect(self.screen, Battery.SILVER, (950, 60, 15, 30))
        pygame.draw.rect(self.screen, Battery.WHITE, (800, 25, 150, 100), 3)
        # pygame.draw.rect(self.screen, Battery.GREEN, (802, 27, 145, 97))
        if self.x != 145:
            pygame.draw.rect(self.screen, Battery.GREEN, (802, 27, self.x, 97))
            self.x += 1


class Text(Battery):
    # def text_objects(text, font):
    #     textSurface = font.render(text, True, RED)
    #     return textSurface, textSurface.get_rect()

    def message_display(self, text):
        largeText = pygame.font.Font("freesansbold.ttf", 20)
        # The text is inside a rectangle and can be referenced by a rectangle.
        textSurface = largeText.render(text, True, self.CYAN)

        # TextSurface, TextRect = text_objects(text, largeText)
        TextRect = textSurface.get_rect()
        TextRect.center = (865, 150)
        self.screen.blit(textSurface, TextRect)


if __name__ == "__main__":
    battery = Battery()
    text = Text()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        battery.draw_rect()
        text.message_display(text="{} %".format(100))
        pygame.display.update()
        battery.clock.tick(60)
