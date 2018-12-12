#   Author: Shankar
#   Date: 12 September 2018
#   Purpose: This program is used to debug and recap of how the original code works.
#   All rights reserved. Refer to the license.txt file.

try:
    import pygame
    import math
    import random
    from pygame.locals import *
    import serial
    import time
except ImportError as ImpErr:
    print("Check your imports !")
    print(str(ImpErr))


class Initialise(object):
    #   Colour definitions (Red ,Green, Blue)
    #   All of the below are called class variables (shared by all instances of the class).
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
    ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=5)


class Speedometer(Initialise):

    def load_image(self):
        self.speedometer_image = pygame.image.load("speed.png")
        self.screen.blit(self.speedometer_image, (100, 5))

    def draw_arc(self,speed_value):
        # pygame.draw.arc()

        # Good example arc below ->
        # pygame.draw.arc(self.screen, Speedometer.YELLOW,
        #                 (235, 75, 525, 525), math.radians(-42), math.radians(223), 4)

        # draw a partial section of an ellipse
        # arc(Surface, color, Rect, start_angle, stop_angle, width=1) -> Rect
        """Draws an elliptical arc on the Surface. The rect argument is the area that the ellipse will fill.
        The two angle arguments are the initial and final
        angle in radians, with the zero on the right. The width argument is the
        thickness to draw the outer edge.

        TAKE NOTE: <Worth mentioning> the initial angle must be less than the final angle; otherwise it will draw the full elipse."""
        pygame.draw.arc(Initialise.screen, Speedometer.YELLOW,
                        (235, 75, 525, 525), math.radians(speed_value), math.radians(224), 5)

class Text(Initialise):
    def message_display(self, text, x_position, y_position):
        largeText = pygame.font.Font("freesansbold.ttf", 20)
        # The text is inside a rectangle and can be referenced by a rectangle.
        textSurface = largeText.render(text, True, Initialise.CYAN)

        # TextSurface, TextRect = text_objects(text, largeText)
        TextRect = textSurface.get_rect()
        TextRect.center = (x_position, y_position)
        Initialise.screen.blit(textSurface, TextRect)


class UpdateValues(Initialise):
    def __init__(self):
        self.speed_value = 30.11
        self.speed_value_original = 25

    def transfer_values(self):
        if (Initialise.ser.in_waiting > 0):
            try:
                values = Initialise.ser.readline()
                print('values',values)
                decoded = values.decode("utf-8")
                print('Decoded',decoded)
                decoded = str(decoded)
                split_decoded = decoded.split(",")

                self.temperature_value_original = float(split_decoded[0].strip())
                self.speed_value_original = float(split_decoded[1].strip())
                self.battery_value_original = float(split_decoded[2].strip())

                self.temperature_value = (-9/2) * self.temperature_value_original + 180
                self.speed_value = (-133/110) * self.speed_value_original + 224
                self.battery_value = self.battery_value_original

                print("Temperature = {}, speed = {}, battery = {}".format(self.temperature_value_original,self.speed_value_original,self.battery_value_original))
            except:
                print("I cannot convert string (Failed to read from DHT sensor) to float")

if __name__ == "__main__":

    initialise = Initialise()

    speedometer = Speedometer()
    speedometer.load_image()

    text = Text()

    updatevalues = UpdateValues()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        initialise.screen.fill(initialise.BLACK)

        speedometer.load_image()
        speedometer.draw_arc(updatevalues.speed_value)

        text.message_display(text="{}".format(
            updatevalues.speed_value_original), x_position=500, y_position=340)

        updatevalues.transfer_values()

        initialise.clock.tick(60)
        pygame.display.update()

pygame.quit()
quit()
