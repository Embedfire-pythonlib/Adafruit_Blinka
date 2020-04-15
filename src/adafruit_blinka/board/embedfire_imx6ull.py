"""Pin definitions for the Embedfire IMX6ULL."""

from adafruit_blinka.microcontroller.nxp_imx6ull import pin


SDA = pin.I2C1_SDA
SCL = pin.I2C1_SCL

PWM1 = pin.PWM1
PWM2 = pin.PWM2
PWM3 = pin.PWM3

R_LED = pin.R_LED_PIN
G_LED = pin.G_LED_PIN
B_LED = pin.B_LED_PIN

BEEP = pin.BEEP_PIN

BUTTON = pin.BUTTON_PIN

MISO = pin.ECSPI3_MISO
MOSI = pin.ECSPI3_MOSI
SCLK = pin.ECSPI3_SCLK
SCK = pin.ECSPI3_SCLK
SS0 = pin.ECSPI3_SS0
DC = pin.ECSPI3_DC
RST = pin.ECSPI3_RST

