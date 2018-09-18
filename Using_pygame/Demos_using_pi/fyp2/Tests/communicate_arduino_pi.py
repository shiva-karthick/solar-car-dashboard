import serial

ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=5)

while True:
    updateCount = 0
    if updateCount < 3:
        if ser.in_waiting > 0:
            values = ser.readline()
            decoded = values.decode("utf-8")
            decoded = str(decoded)
            split_decoded = decoded.split(",")
            
##            for x in split_decoded:
##                print(float(x.rstrip()))
                
            temperature = float(split_decoded[0].rstrip())
            speed = float(split_decoded[1].rstrip())
            battery = float(split_decoded[2].rstrip())

            print("Temperature = {}, speed = {}, battery = {}".format(temperature,speed,battery))
            
    updateCount +=1    

