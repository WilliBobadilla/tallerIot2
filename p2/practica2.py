#author: 
#created_at:
#description: 
#version:

import time
import os
import json
from random import randint
#third part libs
from pushbullet import PushBullet
from dotenv import load_dotenv
try:
    import Adafruit_DHT # libreria para interacturar con dht
except: 
    print("Module Adafruit not found")

load_dotenv() 

class SensorTemp:
    """
    docstring
    """
    TOKEN = os.getenv("TOKEN")
    SIGNAL_PIN = 11 #for rpi


    def __init__(self, set_point, config_push_path):
        self.pb = PushBullet(self.TOKEN)
        self.SET_POINT = set_point # int, si supera el set point, notificar
        push_data = self._read_params(config_push_path)
        self.title = push_data.get('title')
        self.body = push_data.get('body')


    def _read_params(self, file_name):
        """
        """
        with open(file_name,'r') as fil:
            data = json.load(fil)
            print(data)
        return data


    def read_temp(self):
        """
        docstring here
        """
        temp = randint(1,20) #Adafruit_DHT.read_retry(11, 4)
        print(f"Set point es: {self.SET_POINT} C°")
        print(f"temperatura es: {temp} C°")
        if temp > self.SET_POINT:
            self.pb.push_note(self.title, f"{self.body} {temp} C°")
            time.sleep(2)
            print("Message sent")
            #self.turn_on_ac()
        else: 
            pass



if __name__ == '__main__':
    sensor = SensorTemp(10,"config_push.json")
    #implement loop to read the sensor
    sensor.read_temp()
    # https://pastebin.com/Zj8r6n5k

    #pip install pushbullet.py
    #pip install python-dotenv
    #pip install requests