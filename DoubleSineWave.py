# Sine Wave Generator two sine waves 180 degrees out of phase
# y = Offset + A * sin(angle_in_radians) 
import math
import time

A = 40
Offset = 40

for y in range(100):
    for x in range(0, 359, 15):
        radians = 2 * math.pi * x / 360
        index1 = int(Offset + (A * math.sin(radians)))
        index2 = int(Offset + (A * math.sin(radians + math.pi)))
        # calculate a second index by adding PI to the angle_in_radians 
        line = ""
        for j in range(A*2 + 1):
            if j == index1 or j == index2:  # add OR comparison for the second index  
                line = line + "*"
            else:
                line = line + " "
        print(line)
        time.sleep(0.1)
