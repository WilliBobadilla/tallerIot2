#author: 
#created_at:
#description: 
#version:

from time import sleep
import requests
GPIO_ENABLE = False #to verify gpio
try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)

    GPIO_ENABLE = True
except:
    print("gpio not present")



class IssTracker:
    """
    Class to track iss and to alert visually with leds on a rpi
    """
    URL = "http://api.open-notify.org/iss-now.json"
    LED_PIN = 2

    def __init__(self, range_lat, range_lon):
        self.range_lat = range_lat 
        self.range_lon  = range_lon
        if GPIO_ENABLE: 
            GPIO.setup(self.LED_PIN, GPIO.OUT)


    def request_pos(self):
        """
        Method to request position of iss, has to be called on a loop
        to track the iss.
            Params:
                None
            Returns: 
                res (dic): diccionary with the data, see notes
            Notes: 
                res={
                    'timestamp': 1653136410, 
                    'iss_position':{
                        'latitude': '-12.1279', 
                        'longitude': '-129.0742'
                        },
                    'message': 'success'
                    }
        """
        try:
            res = requests.get(self.URL)
            res = res.json()
            return res
        except Exception as e:
            print(str(e))
            return {}

    def verify_pos(self, pos):
        """
        """
        current_lat = float(pos['iss_position']['latitude'])
        current_lon = float(pos['iss_position']['longitude'])
        verify_lat = self.range_lat[0]<current_lat<self.range_lat[1]
        verify_lon = self.range_lon[0]<current_lon<self.range_lon[1]
        print("latitude:", current_lat,"longitude:",current_lon)
        if  verify_lat and verify_lon:
            if GPIO_ENABLE:
                self.toggle_led(self.LED_PIN, True)
            print("En la region!!!!") #turn on the light
        else: 
            if GPIO_ENABLE:
                self.toggle_led(self.LED_PIN, False)
            print("Fuera de la region") #turn off the light


    def toggle_led(self, led, state):
        """
        
        """
        if state:
            GPIO.output(led, GPIO.HIGH)
            print("encendido")
        else: 
            GPIO.output(led, GPIO.LOW)
            print("apagado")



if __name__=='__main__':
    issTracker = IssTracker([-49.52,-45.3433],[-114.00,-90.55]) 
    while True:
        try:
            iss_position = issTracker.request_pos()
            issTracker.verify_pos(iss_position)
            sleep(2)
        except KeyboardInterrupt:
            break 
    print("fin del programa")

