# Lokaverk2022


 -[Rafrásarteikning](https://github.com/SerJunkan/Lokaverk2022/blob/main/circuit%20diagram%20toilet%20sensor.png)
 
 -[Bathroom Network](https://github.com/SerJunkan/Lokaverk2022/blob/main/Bathroom%20Sensor%20Network%20Diagram.png)

<h1>Efnislisti</h1>
  <ul>1x - <a href="https://randomnerdtutorials.com/getting-started-with-esp32/">ESP-32</a></ul>
  <ul>1x - <a href="https://www.raspberrypi.com/products/raspberry-pi-zero/">Raspberry Pi zero</a> en flestir raspi ættu að virka</ul>
  <ul>1x - <a href="https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/how-pirs-work">Pir Hreyfiskynjari</a></ul>
  <ul>1x - <a href="https://www.electroschematics.com/arduino-i2c-lcd-backpack-introductory-tutorial/">l2c lcd skjár með backpack</a> </ul>
  <ul>2x - breadboard</ul>
  <ul>1x - LED</ul>

<h1>Samsettning</h1>
<h3>ESP32</h3>
<p>Ég byrjaði á að tengja PIR skynjaran við ESP32 á breadboardi. GND fer í GND, VCC fer í 5V og OUT fer í GPIO18.</p>
<h3>Söfn notuð í kóða</h3>
  <ul><a href="https://pubsubclient.knolleary.net/">PubSubClient</a></ul>
  <ul><a href="https://www.arduino.cc/reference/en/libraries/wifi/">Wifi</a></ul>
<p>Svo fór ég beint í að skrifa kóðan fyrir MQTT publisherinn, sem má sjá <a href="https://github.com/SerJunkan/Lokaverk2022/blob/main/esp32_publisher.ino">hér</a>.</p>



# Bjargir sem við nýttumst við

https://esp32io.com/tutorials/esp32-motion-sensor


-https://diyi0t.com/microcontroller-to-raspberry-pi-wifi-mqtt-communication/

https://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/#:~:text=Connecting%20an%20I2C%20Enabled%20LCD&text=Connect%20the%20SDA%20pin%20on,of%20the%20Pi%20if%20possible.
