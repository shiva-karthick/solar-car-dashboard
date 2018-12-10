from pyfirmata import Arduino, util
import time

board = Arduino('COM11')

while True:
    print("Turning On")
    board.digital[13].write(1)
    time.sleep(1)
    print("Turning Off")
    board.digital[13].write(0)
    time.sleep(1)

board.exit()
