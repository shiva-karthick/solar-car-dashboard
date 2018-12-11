try:
    import pygame
    import math
    import time
except ImportError:
    print("Check Your imports")

while True:
    data = input()
    # data_decoded = data.decode('utf-8')
    decoded = str(data)
    split_decoded = decoded.split(",")
    data = split_decoded[0].strip()
    temperature = split_decoded[1].strip()
    speed = split_decoded[2].strip()
    battery = split_decoded[3].strip()
    print(data)

    # Guide
    # decoded = values.decode("utf-8")
    # print('Decoded', decoded)
    # decoded = str(decoded)
    # split_decoded = decoded.split(",")

    # data = split_decoded[0].strip()
    # time = split_decoded[1].strip()
