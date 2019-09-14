#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

import qrcode
import qrcode.image.pil

logging.basicConfig(level=logging.DEBUG)

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

try:

    address = str(sys.argv[1])
    print("Address: ", address)
  
    epd = epd2in7.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)

    logging.info("generates qr code")
    qr = qrcode.QRCode(version=4, box_size=4, border=5)
    qr.add_data(address)
    img = qr.make_image(image_factory=qrcode.image.pil.PilImage)
    small_img = img.crop( (0, 0, 150, 150) )
    #small_img.save("qrcode_128x128.bmp")
        
    Himage2 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    #bmp = Image.open(small_img)
    Himage2.paste(small_img, (30,10))
    epd.display(epd.getbuffer(Himage2))
    time.sleep(2)
        

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in7.epdconfig.module_exit()
    exit()
