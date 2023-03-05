from machine import Pin
from ws2812 import WS2812
#from ws2812_auth import WS2812
import time,struct

pin = Pin(2, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np=WS2812(pin)
for i in range(300):
    np.fill(0)
    np.font_set(0x0,0,1,0)
    np.text("MicroPython FrameBuf as WS2812",32-i,0,np.rgb(40,40,0))
    np.show()
    time.sleep_ms(50)
np.fill(0)
np.show()