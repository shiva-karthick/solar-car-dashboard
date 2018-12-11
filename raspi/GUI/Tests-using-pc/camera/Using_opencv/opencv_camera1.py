try:
    import pygame
    import math
    import time
    import random
    # import picamera
    import cv2
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

    pygame.init()
    pygame.display.set_caption("Camera !")
    clock = pygame.time.Clock()
    resolution = (1024, 600)
    screen = pygame.display.set_mode(resolution)


class Camera(Initialise):

    def UseCamera(self):
        cap = cv2.VideoCapture(0)
        # Check if camera opened successfully
        if (cap.isOpened() == False):
            print("Error opening video stream or file")
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            ret = cap.set(3, 320)
            ret = cap.set(4, 240)
            # Removes toolbar and status bar
            # Python: cv2.resizeWindow(winname, width, height) → None
            cv2.resizeWindow("frame", 720, 500)
            cv2.imshow('my webcam', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def stop_preview(self):
            # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    initialise = Initialise()
    camera = Camera()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                camera.UseCamera()
            elif event.type == pygame.K_v:
                camera.stop_preview()

    initialise.clock.tick(60)
    pygame.display.update()

# import cv2
#
#
# def show_webcam(mirror=False):
#     cam = cv2.VideoCapture(0)
#     while True:
#         ret_val, img = cam.read()
#         if mirror:  # normally set to False
#             img = cv2.flip(img, 1)
#         cv2.imshow('my webcam', img)
#         if cv2.waitKey(1) == 27:
#             break  # esc to quit
#     cv2.destroyAllWindows()
#
#
# def main():
#     show_webcam(mirror=True)
#
#
# if __name__ == '__main__':
#     main()
