# Trying to use Open CV to access camera
# Successfully embedded camera , Thanks
try:
    import pygame
    import math
    import time
    import random
    from pygame.locals import *
    import numpy as np
    import sys
    import cv2
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


class Battery(Initialise):

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

    def __init__(self):
        self.a = 200

    def load_image(self):
        self.speedometer_image = pygame.image.load("speed.png")
        self.screen.blit(self.speedometer_image, (100, 5))

    def draw_arc(self):
        # pygame.draw.arc()

        # Good example arc below ->
        # pygame.draw.arc(self.screen, Speedometer.YELLOW,
        # (235, 75, 525, 525), math.radians(-42), math.radians(223), 4)

        # draw a partial section of an ellipse
        # arc(Surface, color, Rect, start_angle, stop_angle, width=1) -> Rect
        """ Draws an elliptical arc on the Surface.
        The rect argument is the area that the ellipse will fill.
        The two angle arguments are the initial and final angle in radians,
        with the zero on the right.
        The width argument is the thickness to draw the outer edge.

        TAKE NOTE: <Worth mentioning>
        the initial angle must be less than the final angle;
        otherwise it will draw the full elipse."""
        pygame.draw.arc(Initialise.screen, Speedometer.YELLOW,
                        (235, 75, 525, 525), math.radians(self.a),
                        math.radians(223), 5)
        if self.a != -42:
            self.a -= 1


class Temperature(Initialise):

    def __init__(self):
        self.a = 179

    def draw_arc(self):
        # pygame.draw.arc()

        # Good example arc below ->
        # pygame.draw.arc(self.screen, Temperature.YELLOW,
        # (235, 75, 525, 525), math.radians(-42), math.radians(223), 4)

        # draw a partial section of an ellipse
        # arc(Surface, color, Rect, start_angle, stop_angle, width=1) -> Rect
        """ Draws an elliptical arc on the Surface.
        The rect argument is the area that the ellipse will fill.
        The two angle arguments are the initial and final angle in radians,
        with the zero on the right.
        The width argument is the thickness to draw the outer edge.

        TAKE NOTE: <Worth mentioning> the initial angle must be less than the
        final angle; otherwise it will draw the full ellipse."""
        pygame.draw.arc(Initialise.screen, Temperature.YELLOW,
                        (50, 75, 200, 200), math.radians(self.a),
                        math.radians(-180), 25)
        if self.a != 0:
            self.a -= 1


class Text(Initialise):
    def message_display(self, text, x_position, y_position):
        largeText = pygame.font.Font("freesansbold.ttf", 20)
        # The text is inside a rectangle and can be referenced by a rectangle.
        textSurface = largeText.render(text, True, Initialise.CYAN)

        # TextSurface, TextRect = text_objects(text, largeText)
        TextRect = textSurface.get_rect()
        TextRect.center = (x_position, y_position)
        Initialise.screen.blit(textSurface, TextRect)


class Camera(Initialise):
    def __init__(self):
        # NOTE -> tutorial link :
        # https://docs.opencv.org/3.0-beta/doc/py_tutorials/
        # py_gui/py_video_display/py_video_display.html

        self.cap = cv2.VideoCapture(0)

        # set the width and height
        self.cap.set(3, 1000)
        self.cap.set(4, 200)

        # Check if camera is opened successfully
        if (self.cap.isOpened() == False):
            print("Error opening video stream or file")

    def use_camera(self):
        # Capture frame-by-frame
        ret, frame = self.cap.read()
        frame = np.rot90(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = pygame.surfarray.make_surface(frame)

        # blit to the screen and set the (x,y) coordinates
        self.screen.blit(frame, (0, 400))

    def stop_preview(self):
        # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":

    initialise = Initialise()

    battery = Battery()

    speedometer = Speedometer()
    speedometer.load_image()

    temperature = Temperature()
    text = Text()

    camera = Camera()

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
                    pass
                elif event.type == pygame.K_q:
                    camera.stop_preview()
                    # The below line requires to be in a While loop
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        camera.stop_preview()

        initialise.screen.fill(initialise.BLACK)

        speedometer.draw_arc()

        battery.draw_rect()

        temperature.draw_arc()

        text.message_display(text="{} %".format(
            100), x_position=865, y_position=150)
        text.message_display(text="{}".format(
            75), x_position=500, y_position=340)

        text.message_display(text="{} degrees".format(
            15), x_position=150, y_position=150)

        camera.use_camera()

        initialise.clock.tick(60)
        pygame.display.update()

pygame.quit()
quit()
