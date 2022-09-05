import board
import displayio
from adafruit_st7789 import ST7789
import gc

#memory is kind of at a premium so lets make sure its not FUBAR
gc.collect()

spi = board.SPI()
    
# Release any resources currently in use for the displays
displayio.release_displays()

tft_cs = board.A4
tft_dc = board.D11

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=board.D10
)

display = ST7789(display_bus, width=240, height=240, rowstart=80)

# Setup the file as the bitmap data source
bitmap = displayio.OnDiskBitmap("/logo_labscon.bmp")

# Create a TileGrid to hold the bitmap
tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

# Create a Group to hold the TileGrid
group = displayio.Group()

# Add the TileGrid to the Group
group.append(tile_grid)

# Add the Group to the Display
display.show(group)

#Loop Forever
while True:
    pass