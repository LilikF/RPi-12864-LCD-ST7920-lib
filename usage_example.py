from st7920 import ST7920
import time 

display=ST7920()

display.initTextMode()

display.examples()
		
for x in range(0,1000):
	display.printStringTextMode(str(x),0,0)
	time.sleep(0.1)