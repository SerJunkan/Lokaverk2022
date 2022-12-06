

import I2C_LCD_driver
from time import *

import paho.mqtt.client as mqtt

import requests

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

MQTT_ADDRESS = '10.201.48.79'
MQTT_USER = 'esp123'
MQTT_PASSWORD = 'esp123'
MQTT_TOPIC = 'home/+/+'

counter = 0 # counter variable

def on_connect(client, userdata, flags, rc):
    """ The callback for when the client receives a CONNACK response from the server."""
    print('Connected with result code ' + str(rc))
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    global counter # you NEED to put the [global] keyword here otherwise u wont be able to "connect" to counter variable
    motion = msg.payload

    mylcd = I2C_LCD_driver.lcd()

    str_pad = " " * 16
    my_long_string = "In Use"
    my_long_string = str_pad + my_long_string

    fixmot = motion.decode("utf-8") # to decode string from esp32
    """The callback for when a PUBLISH message is received from the server."""
    #print(msg.topic + ' ' + str(msg.payload))
    print(fixmot)
    print(counter)
    if fixmot ==  "Motion detected":
        print("LED on")
        GPIO.output(18,GPIO.HIGH)
        #time.sleep(1) important delay if not using for loops
        for i in range (0, len(my_long_string)):
            lcd_text = my_long_string[i:(i+16)]
            mylcd.lcd_display_string(lcd_text,1)
            sleep(0.1) #0.4 til ad lita vel ut
            mylcd.lcd_display_string(str_pad,1)
            mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 2)
        
        if counter >= 5:
            print("notification sent")
            requests.post('https://maker.ifttt.com/trigger/motion_detected/with/key/my8a61TCt1zqacoDxzcdn_aNqs4RCx4gR0IoYEw6XQc')
            counter = 0 
      # counter = counter + 1
    else:
        print("LED off")
        GPIO.output(18,GPIO.LOW)
        counter = counter + 1
        if counter == 5:
            requests.post('https://maker.ifttt.com/trigger/no_motion/with/key/my8a61TCt1zqacoDxzcdn_aNqs4RCx4gR0IoYEw6XQc')
        if counter >= 5:   
            str_pad = " " * 16
            my_long_string = "Available"
            my_long_string = str_pad + my_long_string

            for i in range (0, len(my_long_string)):
                lcd_text = my_long_string[i:(i+16)]
                mylcd.lcd_display_string(lcd_text,1)
                sleep(0.1) #0.4
                mylcd.lcd_display_string(str_pad,1)
                mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 2)
        else:
            my_long_string = "Scanning..."
            my_long_string = str_pad + my_long_string

            for i in range (0, len(my_long_string)):
                lcd_text = my_long_string[i:(i+16)]
                mylcd.lcd_display_string(lcd_text,1)
                sleep(0.1) #0.4
                mylcd.lcd_display_string(str_pad,1)
                mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 2)


def main():
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_ADDRESS, 1883)
    mqtt_client.loop_forever()


if __name__ == '__main__':
    print('MQTT to InfluxDB bridge')
    main()

