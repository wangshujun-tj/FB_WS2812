from micropython import const
import framebuf
from neopixel import NeoPixel
#需要2023年3月以后的固件支持

class WS2812(framebuf.FrameBuffer):   
    def __init__(self, dout): 

        self.dout=dout
        self.width  = 32
        self.height = 8
        self.buffer = bytearray(self.height * self.width*3)
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB888)
        self.np = NeoPixel(self.dout, 256)   # create NeoPixel driver on GPIO0 for 8 pixels
    def show(self):
        for hh in range(self.height):
            for ww in range(self.width):
                if ww%2==0:
                    npindex=ww*self.height+hh
                else:
                    npindex=(ww+1)*self.height-1-hh
                bufindex=hh*self.width+ww
                self.np.buf[npindex*3:npindex*3+3]=self.buffer[bufindex*3:bufindex*3+3]
        self.np.write()            

    def rgb(self,r,g,b):
        return (g<<16)+(r<<8)+b  