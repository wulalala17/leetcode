#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PIL import Image,ImageDraw,ImageFont
import random

msgNum = str(random.randint(1, 99))  # 生成一个指定范围（1-99）整数。

# Read image
im = Image.open('12.png')
w, h = im.size
wDraw = 0.8 * w
hDraw = 0.08 * w

# Draw image
font = ImageFont.truetype('/usr/share/fonts/truetype/droid/DroidSans.ttf', 30) # use absolute font path to fix 'IOError: cannot open resource'
draw = ImageDraw.Draw(im)
draw.text((wDraw, hDraw), msgNum, font=font, fill=(255, 33, 33))

# Save image
im.save('new12.png', 'png')