#!flask/bin/python
from flask import Flask
from flask import request

# Simple demo of of the WS2801/SPI-like addressable RGB LED lights.
import time
import RPi.GPIO as GPIO

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

# Configure the count of pixels:
PIXEL_COUNT = 8

# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)
pixels.clear()
pixels.show()

app = Flask(__name__)

@app.route('/')
@app.route('/led/<int:led>/color')
def index(led):
    print(led)
    r = request.args.get('r', default = 1, type = int)
    g = request.args.get('g', default = 1, type = int)
    b = request.args.get('b', default = 1, type = int)
    pixels.set_pixel(led, Adafruit_WS2801.RGB_to_color( r, b, g ) )
    pixels.show()
    return "{'status':'ok'}"

if __name__ == '__main__':
    app.run(debug=True)
