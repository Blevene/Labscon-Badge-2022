# Labscon-Badge-2022

![alt text](https://github.com/Blevene/Labscon-Badge-2022/blob/main/images/Badge_Live.jpg?raw=true)


## Must use INDEXED bmp files to render on the TFT!

Good tutorial here (though it goes into a bunch of other stuff we don't care about): https://learn.adafruit.com/creating-your-first-tilemap-game-with-circuitpython/indexed-bmp-graphics

## You must add a CircuitPython bootloader to your AdaFruit Feather

## Instructions
Make sure to rename the .py file to code.py or main.py 

You can use most AdaFruit Feather form factor micro-controllers but M0 Express is probably the MINIMUM. 

On your CIRCUITPY drive you need the following folders

1) lib -> this contains third party libraries required to make things work (if you use a non-express board from Adafruit, you may need more libs in this folder)
2) bmp -> this is where your INDEXED bmp files live :-) Use GIMP to convert files to Indexed BMP format. NOTE: The screen is only 240 x 240
3) root folder of the drive should have "code.py"


### Parts used:

1) Adafruit Feather M0 Express - ATSAMD21 Cortex M0: https://www.adafruit.com/product/3403
2) Adafruit 1.54" 240x240 Wide Angle TFT LCD Display with MicroSD - ST7789: https://www.adafruit.com/product/3787
3) Kalih Box Crystal Navy Switches: https://kbdfans.com/products/kailh-box-crystal-navy-clicky-switches

Optional Parts:

1) LiPoly Battery - https://www.adafruit.com/product/1578 -> I used doublesided tape to secure this to the back of the PCB.
2) Tactile On/Off Switch w/Leads - https://www.adafruit.com/product/1092 -> Solder this to EN + Ground Pins on the back of the PCB after soldering the Feather on and you have on/off capabilities!

### Additional non-builtin Libraries Used: 

(these must be in the lib folder on the mounted CIRCUITPYTHON drive)

- adafruit_debouncer
- adafruit_ticks
- adafruit_st7789 

