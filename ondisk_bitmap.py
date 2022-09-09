import board
import os
import displayio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_st7789 import ST7789
from adafruit_debouncer import Debouncer
import gc

# Initialize Switches!
switchL = DigitalInOut(board.D6)
switchL.direction = Direction.INPUT
switchL.pull = Pull.UP
switchL_d = Debouncer(switchL)

switchR = DigitalInOut(board.D5)
switchR.direction = Direction.INPUT
switchR.pull = Pull.UP
switchR_d = Debouncer(switchR)

# memory is kind of at a premium so lets make sure its not FUBAR
gc.collect()

# initalize our SPI connection
spi = board.SPI()

# Release any resources currently in use for the displays
displayio.release_displays()

# Assign the relevant pins for our display
tft_cs = board.A4
tft_dc = board.D11

# instantiate the display bus over FourWire SPI
display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=board.D10
)

# instantiate the display object itself
display = ST7789(display_bus, width=240, height=240, rowstart=80)

# pass name of the selected image and we will render it in the loop
def display_bitmap(image_index):
    while logo_group:
        logo_group.pop()
    bmp_select = f"bmp/{image_index}"
    print(bmp_select)
    bmp = displayio.OnDiskBitmap(bmp_select)
    tile_grid = displayio.TileGrid(bmp, pixel_shader=bmp.pixel_shader)
    logo_group.append(tile_grid)

# Create a Group to hold the Logo
logo_group = displayio.Group()

# Add the Group to the Display
display.show(logo_group)

# Get a list of files in /bmp directory
path = "/bmp"
bmp_list = os.listdir(path)
#[Debug] print(bmp_list)
max_size = len(bmp_list) - 1
#[Debug] print(max_size)

# Takes our button value and uses that as an index for our bitmap last
def shift_image(counter):
    return bmp_list[counter]


# initialize our variables to hold button press states
btn_value = 0
state_change = False

# Loop Forever
while True:
    # check the state of both switches
    switchL_d.update()
    switchR_d.update()

    #Check for Left Switch press
    if switchL_d.fell:
        btn_value -= 1
        state_change = True

    #Check for Right switch press
    if switchR_d.fell:
        btn_value += 1
        state_change = True

    #make sure we don't go out of the range of our list index and also setup for looping around
    if btn_value > max_size or btn_value < -1:
        btn_value = 0

    if state_change == True:
        state_change = False  # reset the state so we dont do this over and over but only on a button press!
        select_image = shift_image(btn_value)
        #{Debug] print(select_image)
        display_bitmap(select_image)