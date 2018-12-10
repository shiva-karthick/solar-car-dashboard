# Lattepanda version
# Author: Shankar
# Date: 12 September 2018
# Purpose: This code is a dashboard for a solar vehicle. Refer to README
# All rights reserved.

try:
    import pygame
    import math
    import random
    # import picamera
    from pygame.locals import *
    # import serial
    import time
except ImportError as ImpErr:
    print("Check your imports !")
    print(str(ImpErr))


class Initialise(object):
    # Colour definitions (Red ,Green, Blue)
    # All the below code are class variables
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
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    # ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=5)


class Text(Initialise):
    def message_display(self, text, x_position, y_position):
        largeText = pygame.font.Font("freesansbold.ttf", 20)
        # The text is inside a rectangle and can be referenced by a rectangle.
        textSurface = largeText.render(text, True, Initialise.CYAN)

        # TextSurface, TextRect = text_objects(text, largeText)
        TextRect = textSurface.get_rect()
        TextRect.center = (x_position, y_position)
        Initialise.screen.blit(textSurface, TextRect)


class Battery(Text):
    def draw_rect(self, battery_value):
        pygame.draw.rect(Initialise.screen, Battery.SILVER, (956, 65, 15, 30))
        pygame.draw.rect(Initialise.screen, Battery.WHITE,
                         (800, 25, 158, 120), 3)

        # pygame.draw.rect(screen, color, (x,y,width,height), thickness)
        # pygame.draw.rect(self.screen, Battery.GREEN, (802, 27, 145, 97))
        if (battery_value > 70 and battery_value <= 140):
            pygame.draw.rect(Initialise.screen, Initialise.GREEN,
                             (802, 27, battery_value, 117))
        elif ((battery_value > 42) and (battery_value <= 70)):
            pygame.draw.rect(Initialise.screen, Battery.YELLOW,
                             (802, 27, battery_value, 117))
        elif (battery_value >= 0 and battery_value <= 42):
            pygame.draw.rect(Initialise.screen, Initialise.RED,
                             (802, 27, battery_value, 117))
            self.bolt_image = pygame.image.load("bolted.png")
            self.bolt_image = pygame.transform.scale(
                self.bolt_image, (100, 110))
            Initialise.screen.blit(self.bolt_image, (830, 33))
            Text.message_display(self, text="LOW Battery !!!",
                                 x_position=865, y_position=200)


class Speedometer(Initialise):
    def load_image(self):
        self.speedometer_image = pygame.image.load("speed.png")
        self.speedometer_image = pygame.transform.scale(
            self.speedometer_image, (700, 450))
        Initialise.screen.blit(self.speedometer_image, (155, -40))

    def draw_arc(self, speed_value):
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
                        (277, 5, 450, 400), math.radians(speed_value), math.radians(224), 5)


class Temperature(Text):
    def draw_arc(self, temperature_value):

        # Good example arc below ->
        # pygame.draw.arc(Initialise.screen, Initialise.YELLOW, (50, 75,
        # 200, 200), math.radians(0), math.radians(180), 4)

        # draw a partial section of an ellipse
        # arc(Surface, color, Rect, start_angle, stop_angle, width=1) -> Rect
        """Draws an elliptical arc on the Surface. The rect argument is the area that the ellipse will fill.
    The two angle arguments are the initial and final angle in radians,
    with the zero on the right. The width argument is the thickness to draw the outer edge.

        TAKE NOTE: <Worth mentioning> the initial angle must be less
        than the final angle; otherwise it will draw the full elipse."""
        if (temperature_value >= 0 and temperature_value < 45):
            pygame.draw.arc(Initialise.screen, Initialise.RED, (10, 75, 250, 250), math.radians(
                temperature_value), math.radians(180), 25)
            Text.message_display(
                self, text="HIGH Temperature !!!", x_position=150, y_position=235)

            self.high_temperature_image = pygame.image.load("temperature.jpg")
            self.high_temperature_image = pygame.transform.scale(
                self.high_temperature_image, (50, 50))
            Initialise.screen.blit(self.high_temperature_image, (115, 125))

        elif (temperature_value >= 45 and temperature_value < 135):
            pygame.draw.arc(Initialise.screen, Initialise.YELLOW, (10, 75, 250, 250), math.radians(
                temperature_value), math.radians(180), 25)
        elif(temperature_value >= 135):
            pygame.draw.arc(Initialise.screen, Initialise.GREEN, (10, 75, 250, 250), math.radians(
                temperature_value), math.radians(180), 25)
            Text.message_display(
                self, text="LOW Temperature !!!", x_position=150, y_position=250)


class Camera(Initialise):
    # The below are declared as class variables
    camera_position = (0, 300, 1024, 300)
    camera_block = pygame.Surface((1024, 300))

    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.preview_fullscreen = False
        self.camera.preview_window = (0, 350, 1024, 300)
        self.camera.resolution = (1024, 300)

    def use_camera(self):
        # If your preview is upside-down, you can rotate it with the following code
        # self.camera.rotation = 180
        self.camera.start_preview()
        Initialise.screen.blit(
            Camera.camera_block, (Camera.camera_position[0], Camera.camera_position[1]))

    def stop_camera(self):
        self.camera.stop_preview()


class UpdateValues(Initialise):
    def __init__(self):
        self.temperature_value = 4.5
        self.temperature_value_original = 39

        self.speed_value = 30.11
        self.speed_value_original = 25

        self.battery_value = 135
        self.battery_value_original = 75

    def transferValues(self):
        if (Initialise.ser.in_waiting):
            try:
                values = Initialise.ser.readline()
                print('values', values)
                decoded = values.decode("utf-8")
                print('Decoded', decoded)
                decoded = str(decoded)
                split_decoded = decoded.split(",")

                self.data = split_decoded[0].strip()
                self.time = split_decoded[1].strip()
                self.temperature_value_original = float(
                    split_decoded[2].strip())
                self.speed_value_original = float(split_decoded[3].strip())
                self.battery_value_original = float(split_decoded[4].strip())
                self.current_1 = float(split_decoded[5].strip())
                self.current_2 = float(split_decoded[6].strip())
                self.current_3 = float(split_decoded[7].strip())
                self.current_4 = float(split_decoded[8].strip())
                self.current_5 = float(split_decoded[9].strip())

                # data = split_decoded[0].strip()
                # time = split_decoded[1].strip()
                # temperature = float(split_decoded[2].strip())
                # speed = float(split_decoded[3].strip())
                # battery = float(split_decoded[4].strip())
                # current = float(split_decoded[5].strip())

                self.temperature_value = (-9/2 *
                                          self.temperature_value_original) + 180
                self.speed_value = (-133/110 * self.speed_value_original) + 224
                self.battery_value = self.battery_value_original

                print("Temperature = {}, speed = {}, battery = {}".format(
                    self.temperature_value_original, self.speed_value_original, self.battery_value_original))
            except:
                print(
                    "I cannot convert string (Failed to read from DHT sensor) to float")


if __name__ == "__main__":

    initialise = Initialise()

    battery = Battery()

    speedometer = Speedometer()
    speedometer.load_image()

    temperature = Temperature()

    text = Text()

    camera = Camera()

    updatevalues = UpdateValues()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    initialise.resolution = (1024, 600)
                    initialise.screen = pygame.display.set_mode(
                        initialise.resolution, pygame.FULLSCREEN)
                elif event.key == pygame.K_g:
                    initialise.resolution = (1024, 600)
                    initialise.screen = pygame.display.set_mode(
                        initialise.resolution, pygame.RESIZABLE)
                elif event.key == pygame.K_c:
                    camera.use_camera()
                elif event.key == pygame.K_v:
                    camera.stop_camera()

        initialise.screen.fill(initialise.BLACK)

        speedometer.load_image()
        speedometer.draw_arc(updatevalues.speed_value)

        battery.draw_rect(updatevalues.battery_value_original)

        temperature.draw_arc(updatevalues.temperature_value)

        text.message_display(text="{} Volts".format(
            updatevalues.battery_value_original), x_position=865, y_position=175)

        text.message_display(text="{}".format(
            updatevalues.speed_value_original), x_position=500, y_position=200)

        text.message_display(text="{} degrees".format(
            updatevalues.temperature_value_original), x_position=150, y_position=200)

        updatevalues.transferValues()

        initialise.clock.tick(60)
        pygame.display.update()

pygame.quit()
quit()
