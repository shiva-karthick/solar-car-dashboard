from pyfirmata import Arduino, util
import time

board = Arduino('COM11', baudrate=57600)
iterator = util.Iterator(board)
iterator.start()

while True:

    time.sleep(1)

board.exit()
