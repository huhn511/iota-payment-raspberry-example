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
import traceback

import qrcode
import qrcode.image.pil

logging.basicConfig(level=logging.DEBUG)

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

try:
  
    epd = epd2in7.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)

    font24 = ImageFont.truetype(os.path.join(
        picdir, 'RobotoSlab-Regular.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(
        picdir, 'RobotoSlab-Regular.ttc'), 18)

    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    Himage = Image.new('1', (epd.height, epd.width),
                       255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    draw.text((60, 10), 'Thanks for the payment!', font=font24, fill=0)
    draw.text((10, 80), 'Your payment was successfully paid.',
              font=font18, fill=0)

    epd.display(epd.getbuffer(Himage))
        

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in7.epdconfig.module_exit()
    exit()
