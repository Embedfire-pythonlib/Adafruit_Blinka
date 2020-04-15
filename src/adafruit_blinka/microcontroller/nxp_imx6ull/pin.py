from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin

I2C1_SCL = Pin((0, 28)) # GPIO1_IO28
I2C1_SDA = Pin((0, 29)) # GPIO1_IO29

I2C2_SCL = Pin(0) # GPIO1_IO0
I2C2_SDA = Pin(1) # GPIO1_IO1

PWM1 = Pin((0, 1))      # GPIO1_IO01
PWM2 = Pin((0, 13))     # GPIO1_IO13
PWM3 = Pin((0, 14))    # GPIO1_IO14

R_LED_PIN = Pin((0, 4))    # GPIO1_IO4
G_LED_PIN = Pin((3, 20))    # GPIO4_IO20
B_LED_PIN = Pin((3, 19))    # GPIO4_IO19
BEEP_PIN = Pin((0, 19))    # GPIO1_IO19

BUTTON_PIN = Pin((4, 1))    # GPIO5_IO1

ECSPI3_MISO = Pin(23) # IO1_23
ECSPI3_MOSI = Pin(22) # IO1_22 
ECSPI3_SCLK = Pin(21) # IO1_21
ECSPI3_SS0 = Pin(20)  # IO1_20 
ECSPI3_DC = Pin(18) # IO1_18
ECSPI3_RST = Pin(17)  # IO1_17

i2cPorts = ( (0, I2C1_SCL, I2C1_SDA), (2, I2C2_SCL, I2C2_SDA),)
# ordered as spiId, sckId, mosiId, misoId
spiPorts = ( (2, ECSPI3_SCLK, ECSPI3_MOSI, ECSPI3_MISO), )
# SysFS pwm outputs, pwm channel and pin in first tuple
pwmOuts = ( ((0, 0), PWM1), ((1, 0), PWM2), ((2, 0), PWM3), )

# UART1_TXD/RXD on /dev/ttymxc0
# UART3_TXD/RXD not available (?)
