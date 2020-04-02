from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin

I2C1_SCL = Pin((0, 28)) # GPIO1_IO28
I2C1_SDA = Pin((0, 29)) # GPIO1_IO29

I2C2_SCL = Pin(0) # GPIO1_IO0
I2C2_SDA = Pin(1) # GPIO1_IO1

D0 = Pin(0)
D1 = Pin(1)
D2 = Pin(2)
D3 = Pin(3)
D4 = Pin(4)

PWM1 = Pin((0, 1))      # GPIO1_IO01
PWM2 = Pin((0, 13))     # GPIO1_IO13
PWM3 = Pin((0, 14))    # GPIO1_IO14

GPIO6 = Pin((0, 6))     # GPIO1_IO6
GPIO7 = Pin((0, 7))     # GPIO1_IO7
GPIO8 = Pin((0, 8))     # GPIO1_IO8
GPIO73 = Pin((2, 9))    # GPIO3_IO9
GPIO77 = Pin((2, 13))   # GPIO3_IO13
GPIO138 = Pin((4, 10))  # GPIO5_IO10 
GPIO141 = Pin((4, 13))  # GPIO5_IO13

ECSPI1_MISO = Pin(136) # GPIO5_IO8
ECSPI1_MOSI = Pin(135) # GPIO5_IO7 
ECSPI1_SCLK = Pin(134) # GPIO5_IO6
ECSPI1_SS0 = Pin(133)  # GPIO5_IO9 


i2cPorts = ( (0, I2C1_SCL, I2C1_SDA), (2, I2C2_SCL, I2C2_SDA),)
# ordered as spiId, sckId, mosiId, misoId
spiPorts = ( (32766, ECSPI1_SCLK, ECSPI1_MOSI, ECSPI1_MISO), )
# SysFS pwm outputs, pwm channel and pin in first tuple
pwmOuts = ( ((0, 0), PWM1), ((1, 0), PWM2), ((2, 0), PWM3), )

# UART1_TXD/RXD on /dev/ttymxc0
# UART3_TXD/RXD not available (?)
