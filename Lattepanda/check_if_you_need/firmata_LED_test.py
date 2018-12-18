# import pyfirmata

# led_pin = 7

# board = pyfirmata.ArduinoMega("com6")

# while True:
#     print("Turning On")
#     board.digital[led_pin].write(1)
#     board.pass_time(1)
#     print("Turning Off")
#     board.digital[led_pin].write(0)
#     board.pass_time(1)

from pyfirmata import ArduinoMega, util
import time

board = ArduinoMega('COM6')

while True:
    print("Turning On")
    board.digital[13].write(1)
    time.sleep(1)
    print("Turning Off")
    board.digital[13].write(0)
    time.sleep(1)
