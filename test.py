import time 
import autoit

time.sleep(5)
for x in range(2):
    autoit.mouse_click("left", 0, 0, 1)
    time.sleep(4)
