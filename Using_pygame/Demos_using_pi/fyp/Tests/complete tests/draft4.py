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
    ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=5)


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
        self.x = 0

    def draw_rect(self):
        pygame.draw.rect(Initialise.screen, Battery.SILVER, (950, 60, 15, 30))
        pygame.draw.rect(Initialise.screen, Battery.WHITE,
                         (800, 25, 150, 100), 3)
        # pygame.draw.rect(self.screen, Battery.GREEN, (802, 27, 145, 97))
        if self.x != 145:
            pygame.draw.rect(self.screen, Battery.GREEN, (802, 27, self.x, 97))
            self.x += 1
        # pygame.draw.rect(Initialise.screen, Battery.GREEN,
        #                  (802, 27, self.x, 97))


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

##    def __init__(self):
##        self.a = 200

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
        """Draws an elliptical arc on the Surface. The rect argument is the area that the ellipse will fill. The two angle arguments are the initial and final
angle in radians, with the zero on the right. The width argument is the
thickness to draw the outer edge.

        TAKE NOTE: <Worth mentioning> the initial angle must be less than the final angle; otherwise it will draw the full elipse."""
        pygame.draw.arc(Initialise.screen, Speedometer.YELLOW,
                        (235, 75, 525, 525), math.radians(speed_value), math.radians(224), 5)
##        if self.a != -42:
##            self.a -= 1


class Temperature(Initialise):
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

##    def __init__(self):
##        self.a = 180
##        pass

    def draw_arc(self,temperature_value):
        # pygame.draw.arc()

        # Good example arc below ->
        # pygame.draw.arc(self.screen, Temperature.YELLOW,
        #                 (235, 75, 525, 525), math.radians(-42), math.radians(223), 4)

        # draw a partial section of an ellipse
        # arc(Surface, color, Rect, start_angle, stop_angle, width=1) -> Rect
        """Draws an elliptical arc on the Surface. The rect argument is the area that the ellipse will fill.
The two angle arguments are the initial and final angle in radians,
with the zero on the right. The width argument is the thickness to draw the outer edge.

        TAKE NOTE: <Worth mentioning> the initial angle must be less than the final angle; otherwise it will draw the full elipse."""
        pygame.draw.arc(Initialise.screen, Temperature.YELLOW,
                        (50, 75, 200, 200), math.radians(float(temperature_value)), math.radians(-180), 25)
##        if self.a != 0:
##            self.a -= 1


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
        self.temperature_value = 135
        self.temperature_value_original = 30

        self.speed_value = 30.11
        self.speed_value_original = 25
##
##        self.battery_value = 135
##        self.battery_value_original = 75

    def temperature(self):
        updateCount = 0
        if updateCount < 3:
            if Initialise.ser.in_waiting > 0:
                try:
                    values = Initialise.ser.readline()
                    decoded = values.decode("utf-8")
                    decoded = str(decoded)
                    split_decoded = decoded.split(",")

                    self.temperature_value_original = float(split_decoded[0].rstrip())
                    self.speed_value_original = float(split_decoded[1].rstrip())
                    self.battery_value_original = float(split_decoded[2].rstrip())

                    self.temperature_value = (-9/2) * self.temperature_value_original + 180
                    self.speed_value = (-133/110) * self.speed_value_original + 224


                    print("Temperature = {}, speed = {}, battery = {}".format(self.temperature_value_original,self.speed_value_original,self.battery_value_original))
                except:
                    print("I cannot convert string (Failed to read from DHT sensor) to float")
        updateCount +=1



if __name__ == "__main__":

    initialise = Initialise()

    battery = Battery()

    speedometer = Speedometer()
    speedometer.load_image()

    temperature = Temperature()

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

        battery.draw_rect()

        temperature.draw_arc(updatevalues.temperature_value)

        text.message_display(text="{} %".format(
            100), x_position=865, y_position=150)
        text.message_display(text="{}".format(
            updatevalues.speed_value_original), x_position=500, y_position=340)

        text.message_display(text="{} degrees".format(
            updatevalues.temperature_value_original), x_position=150, y_position=150)

        updatevalues.temperature()

        initialise.clock.tick(60)
        pygame.display.update()

pygame.quit()
quit()
