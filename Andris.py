#All credit goes to Eric unless specified otherwise.



import RPi.GPIO as GPIO
from time import sleep

red = 10  # GPIO number where the led is connected
green = 22
blue = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# Blink some leds
# while True:
#     GPIO.output(red, False)
#     sleep(1)  # Sleep for 1 second
#     GPIO.output(red, False)
#     GPIO.output(blue, True)
#     sleep(1)
#     GPIO.output(blue, False)
#     GPIO.output(green, True)
#     sleep(1)
#     GPIO.output(green, False)
def cleanLed():
  GPIO.output(red, True)
  GPIO.output(blue, True)
  GPIO.output(green, True)

def redOn():
  GPIO.output(red, False)

def blueOn():
  GPIO.output(blue, False)

def greenOn():
  GPIO.output(green, False)

# def main():
#   cleanLed()
#   blueOn()

# if __name__ == "__main__":
#     main()

