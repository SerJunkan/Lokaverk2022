

import I2C_LCD_driver
from time import *

import paho.mqtt.client as mqtt

import requests

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT) #pin for LED

MQTT_ADDRESS = '10.201.48.79' #Ip address of the rasberrypi zero in our case the raspi ip is 10.201.48.79 but NOTE: it might change when wifi is reset or full
MQTT_USER = 'USERNAME' #MQTT USERNAME AND PASSWORD
MQTT_PASSWORD = 'PASSWORD'
MQTT_TOPIC = 'home/+/+' #MQTT topic (NOT NEEDED IN THIS CODE)

counter = 0 # counter variable

def on_connect(client, userdata, flags, rc): #Subscriber
    print('Connected with result code ' + str(rc))
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg): 
    global counter # you NEED to put the [global] keyword here otherwise u wont be able to "connect" to counter variable mentioned erlier
    motion = msg.payload

    mylcd = I2C_LCD_driver.lcd()

    str_pad = " " * 16
    my_long_string = "In Use" #my_long_string is string variable printed on l2c LCD
    my_long_string = str_pad + my_long_string

    fixmot = motion.decode("utf-8") # to decode string from esp32
    #print(msg.topic + ' ' + str(msg.payload)) example of topic use if u want to use topic
    print(fixmot) #prints string decoded from esp-32
    print(counter) #prints value of counter variable (mostly for debugging)
    if fixmot ==  "Motion detected": 
        print("LED on")
        GPIO.output(18,GPIO.HIGH)
        #time.sleep(1) important delay if NOT using for loops
        for i in range (0, len(my_long_string)): #For loop to display time and to make string variable scroll
            lcd_text = my_long_string[i:(i+16)]
            mylcd.lcd_display_string(lcd_text,1)
            sleep(0.1) #0.4 delay is reccomended to make scrolling text look good but in our case it makes code run too slow :(
            mylcd.lcd_display_string(str_pad,1)
            mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 2) #displaying time in Hours/Min/Secs 
        
        if counter >= 5: #counter in use so user isisnt spammed with notifications
            print("notification sent")
            requests.post('https://maker.ifttt.com/trigger/[OPERATION NAME]/with/key/[INSERT YOUR KEY HERE]') 
            counter = 0 # using iftt to send notifacation to users phone whether or not Bathroom is available NOTE:do not use the brackets []
    else:
        print("LED off")
        GPIO.output(18,GPIO.LOW)
        counter = counter + 1
        if counter == 5: #spam countermesure
            requests.post('https://maker.ifttt.com/trigger/[OPERATION NAME]/with/key/[INSERT YOUR KEY HERE]')
        if counter >= 5:   
            str_pad = " " * 16
            my_long_string = "Available" #changing string value
            my_long_string = str_pad + my_long_string

            for i in range (0, len(my_long_string)): #scroll
                lcd_text = my_long_string[i:(i+16)]
                mylcd.lcd_display_string(lcd_text,1)
                sleep(0.1) #0.4
                mylcd.lcd_display_string(str_pad,1)
                mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 2) #time
        else:
            my_long_string = "Scanning..." #default state text used as a buffer in case for example toilet user is completly still for a few moments 
            my_long_string = str_pad + my_long_string

            for i in range (0, len(my_long_string)):
                lcd_text = my_long_string[i:(i+16)]
                mylcd.lcd_display_string(lcd_text,1)
                sleep(0.1) #0.4
                mylcd.lcd_display_string(str_pad,1)
                mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 2) #time 


def main(): #main loop
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_ADDRESS, 1883)
    mqtt_client.loop_forever()


if __name__ == '__main__':
    print('MQTT to InfluxDB bridge')
    main()

