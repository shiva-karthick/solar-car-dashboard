from pyfirmata import Arduino, util
import time

board = Arduino('COM5')
it = util.Iterator(board)
it.start()
board.analog[5].enable_reporting()

while True:
    print((board.analog[5].read() / 1023) * 5)






    