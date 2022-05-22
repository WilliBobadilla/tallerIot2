import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)

while True:
        GPIO.output(2, GPIO.HIGH)
        sleep(1)
        GPIO.output(2,GPIO.LOW)
        sleep(1)
