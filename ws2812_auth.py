from micropython import const
import framebuf
from neopixel import NeoPixel
#用原版固件需要的写法 


class WS2812(framebuf.FrameBuffer):   
    def __init__(self, dout): 

        self.dout=dout
        self.width  = 32
        self.height = 8

        self.buffer = bytearray(self.height * self.width*2)
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)
        self.np = NeoPixel(self.dout, 256)   # create NeoPixel driver on GPIO0 for 8 pixels
    def show(self):
        for hh in range(self.height):
            for ww in range(self.width):
                if ww%2==0:
                    npindex=ww*self.height+hh
                else:
                    npindex=(ww+1)*self.height-1-hh
                p=self.pixel(ww,hh)
                self.np[npindex]=((p&0xf800)>>8,(p&0x07E0)>>3,(p&0x001F)<<3)
        self.np.write()
    def rgb(self,r,g,b):
        return ((r&0xf8)<<8)+((g&0xfc)<<3)+((b&0xf8)>>3)

        