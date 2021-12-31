#!/usr/bin/env python3
import time
from rpi_ws281x import *
from PIL import Image, ImageDraw
import os

# LED strip configuration:
LED_COUNT      = 384      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 40      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
WAIT_COUNT     = 3
BASE_PATH      = '/home/pi/pixart/'

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

try:
    positions = [[376, 377, 378, 379, 380, 381, 382, 383, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319],
                 [375, 374, 373, 372, 371, 370, 369, 368, 303, 302, 301, 300, 299, 298, 297, 296, 295, 294, 293, 292, 291, 290, 289, 288],
                 [360, 361, 362, 363, 364, 365, 366, 367, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287],
                 [359, 358, 357, 356, 355, 354, 353, 352, 271, 270, 269, 268, 267, 266, 265, 264, 263, 262, 261, 260, 259, 258, 257, 256],
                 [344, 345, 346, 347, 348, 349, 350, 351, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255],
                 [343, 342, 341, 340, 339, 338, 337, 336, 239, 238, 237, 236, 235, 234, 233, 232, 231, 230, 229, 228, 227, 226, 225, 224],
                 [328, 329, 330, 331, 332, 333, 334, 335, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223],
                 [327, 326, 325, 324, 323, 322, 321, 320, 207, 206, 205, 204, 203, 202, 201, 200, 199, 198, 197, 196, 195, 194, 193, 192],
                 [56, 57, 58, 59, 60, 61, 62, 63, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191],
                 [55, 54, 53, 52, 51, 50, 49, 48, 175, 174, 173, 172, 171, 170, 169, 168, 167, 166, 165, 164, 163, 162, 161, 160],
                 [40, 41, 42, 43, 44, 45, 46, 47, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159],
                 [39, 38, 37, 36, 35, 34, 33, 32, 143, 142, 141, 140, 139, 138, 137, 136, 135, 134, 133, 132, 131, 130, 129, 128],
                 [24, 25, 26, 27, 28, 29, 30, 31, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127],
                 [23, 22, 21, 20, 19, 18, 17, 16, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96],
                 [8, 9, 10, 11, 12, 13, 14, 15, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95],
                 [7, 6, 5, 4, 3, 2, 1, 0, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64]]
    
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    colorWipe(strip, Color(0,0,0), 0)
    
    for file in sorted(os.listdir(BASE_PATH)):
        if not file.endswith("png"):
            continue
        
        print (file)
        img = Image.open(BASE_PATH + file)
        img = img.convert("RGB")
    
        for x in range(img.width):
            for y in range(img.height):
                r = img.getpixel((x, y))[0]
                g = img.getpixel((x, y))[1]
                b = img.getpixel((x, y))[2] 
                strip.setPixelColor(positions[x][y], Color(r, g, b))
                #strip.setPixelColor(positions[x][y], 0)
                #time.sleep(50/1000.0)
            strip.show()
        time.sleep(WAIT_COUNT)
        
    colorWipe(strip, Color(0,0,0), 0)
    
    #strip.setPixelColor(positions[3][2], Color(0, 0, 255))
    
    #strip.show()
except KeyboardInterrupt:
    colorWipe(strip, Color(0,0,0), 0)