# Lokaverk2022


<h1>Efnislisti</h1>
  <ul>1x - <a href="https://randomnerdtutorials.com/getting-started-with-esp32/">ESP-32</a></ul>
  <ul>1x - <a href="https://www.raspberrypi.com/products/raspberry-pi-zero/">Raspberry Pi zero</a> en flestir raspi ættu að virka</ul>
  <ul>1x - <a href="https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/how-pirs-work">Pir Hreyfiskynjari</a></ul>
  <ul>1x - <a href="https://www.electroschematics.com/arduino-i2c-lcd-backpack-introductory-tutorial/">l2c lcd skjár með backpack</a> </ul>
  <ul>2x - breadboard</ul>
  <ul>1x - LED</ul>
  

  <h2>Skýringamyndir fyrir Rafrásir og Nettengingar</h2>
  
      
 -[Rafrásarteikning](https://github.com/SerJunkan/Lokaverk2022/blob/main/circuit%20diagram%20toilet%20sensor.png)
 
 -[Bathroom Network](https://github.com/SerJunkan/Lokaverk2022/blob/main/Main%20Network%20Diagram.png)

<h1>Samsetning</h1>
<h3>ESP32</h3>
<p>Við byrjuðum á að tengja PIR skynjaran við ESP32 með breadboardi. [GND fer í GND | VCC fer í 5V | OUT fer í GPIO18].</p>
<p>Svo fórum við beint í að skrifa kóðan fyrir MQTT tengingu, sem má sjá <a href="https://github.com/SerJunkan/Lokaverk2022/blob/main/esp32_publisher.ino">hér</a>.</p>
<p>við lentum ekki í miklu veseni með Esp annað en eitt atvik af stilla upload speed og í lokinn þegar við þurftum að viljandi hægja á kóðanum þarsem for lykkjurnar í rassberry hægðu rosa mikið á kóðanum, sem gerði það að verkum að Raspi var "overloaded" af ESP og tók alltaf lengri tíma til að höndla Satus gönin sem Esp var að senda inn (svo ef þú villt hafa hraðann kóða losnaðu bara við for loopin)</p>
<p>við lentum hinsvegar í ansi mikklu veseni varðandi PIR skynjarann þarsem það þurfti að Fínstylla hann (bæði refresh rate og signal lenght) ásamt því að annar skynjarinn virkaði spes af einhverjum ástæðum en að enda reddaðist það og skynjarinn virkaði einsog ætlað.</p>

<h3>RasberryPi-Zero</h3>


<h3>Söfn notuð í ESP-32 kóða</h3>
  <ul><a href="https://pubsubclient.knolleary.net/">PubSubClient</a></ul>
  <ul><a href="https://www.arduino.cc/reference/en/libraries/wifi/">Wifi</a></ul>
  
<h3>Söfn notuð í RAPSPI kóða</h3>
  <ul><a href="https://pypi.org/project/paho-mqtt/">Paho-MQTT</a></ul>
  <ul><a href="https://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/#:~:text=Connecting%20an%20I2C%20Enabled%20LCD&text=Connect%20the%20SDA%20pin%20on,of%20the%20Pi%20if%20possible."> I2C_LCD_driver</a> Note!: það þarf að setja kóða (sem hægt er að finna í hlekk) í py skrá á sama stað og aðalkóði.py á rasberri</ul>
  <ul><a href="https://pypi.org/project/requests/">Requests</a></ul>
  <ul><a href="https://pypi.org/project/RPi.GPIO/">Requests</a></ul>
  <ul><a href="https://docs.python.org/3/library/time.html">Time</a></ul>


# Myndir af Tengingum

![alt text](https://github.com/SerJunkan/Lokaverk2022/blob/main/connections/Tenging1.jpg)
![alt text](https://github.com/SerJunkan/Lokaverk2022/blob/main/connections/Tenging2.jpg)
![alt text](https://github.com/SerJunkan/Lokaverk2022/blob/main/connections/Tenging3.jpg)
![alt text](https://github.com/SerJunkan/Lokaverk2022/blob/main/connections/Tenging4.jpg)
![alt text](https://github.com/SerJunkan/Lokaverk2022/blob/main/connections/Tenging5.jpg)
![alt text](https://github.com/SerJunkan/Lokaverk2022/blob/main/connections/Tenging6.jpg)


# Bjargir sem við nýttumst við

-https://esp32io.com/tutorials/esp32-motion-sensor

-https://diyi0t.com/microcontroller-to-raspberry-pi-wifi-mqtt-communication/

-https://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/#:~:text=Connecting%20an%20I2C%20Enabled%20LCD&text=Connect%20the%20SDA%20pin%20on,of%20the%20Pi%20if%20possible.
