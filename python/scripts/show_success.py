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


try:

    epd = epd2in7.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)

    font24 = ImageFont.truetype(os.path.join(
        picdir, 'RobotoSlab-Regular.ttf'), 24)
    font18 = ImageFont.truetype(os.path.join(
        picdir, 'RobotoSlab-Regular.ttf'), 18)
    
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 50), 'Payment success! :-)', font = font24, fill = 0)
    
    epd.display(epd.getbuffer(Himage))
    time.sleep(10)
    epd.Clear(0xFF)

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in7.epdconfig.module_exit()
    exit()
