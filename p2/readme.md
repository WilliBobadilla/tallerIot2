# Practice 2 
Interactuar con el sensor DHT11, realizar un programa que lea el 
sensor dht11 y luego, notificar si algun alguna medicion esta fuera
de rango.

# Instrucciones
Al leer una temperatura superior al set point, emitir una alerta a la app.

# Desafio 

1. Poner como parametro si se debe de verificar mayor o menor temperatura al set point
al instanciar la clase.  Por ejemplo: 

    ```
    SensorTemp(10,"menor que","config_push.json") # entonces la temp debe ser menor que 10 para alertar
    ```

# App a utilizar 
* https://www.pushbullet.com/


# Requirements
* pushbullet.py
* python-dotenv