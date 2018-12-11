try:
    import pygame
    import time
    import math
except ImportError:
    pass

if __name__ == "__main__":
    while True:
        print("Temperature {}".format(25))
        print("Speed {}".format(100))
        print("Battery Voltage {}".format(75))
        time.sleep(5)
