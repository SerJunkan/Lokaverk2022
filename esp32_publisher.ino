#include "PubSubClient.h"

#include "WiFi.h"

const char* ssid = "TskoliVESM";                 // Vesm SSID
const char* wifi_password = "Fallegurhestur"; // Vesm password

const char* mqtt_server = "10.201.48.79";  // IP of the MQTT broker
const char* bathroom_topic = "home/bathroom/status"; // Ekki notað
const char* mqtt_username = "username"; // MQTT username
const char* mqtt_password = "password"; // MQTT password
const char* clientID = "clientID"; // MQTT client ID


const int PIN_TO_SENSOR = 18; // GIOP18 pin connected to OUTPUT pin of sensor
int pinState   = LOW;  // current state of pin

WiFiClient wifiClient;
// 1883 er listener port fyrir Brokerinn
PubSubClient client(mqtt_server, 1883, wifiClient); 


// Fall sem tengir sig við mqtt í gegnum netið
void connect_MQTT(){
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, wifi_password); //Tengir sig við netið

  // Biður eftir að tenginginn hefur verið staðfest
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  // Debugging - Output the IP Address of the ESP8266
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  // Tengir sig við MQTT Broker
  if (client.connect(clientID, mqtt_username, mqtt_password)) {
    Serial.println("Connected to MQTT Broker!");
  }
  else {
    Serial.println("Connection to MQTT Broker failed...");
  }
}


void setup() {
  Serial.begin(115200);
  connect_MQTT(); //Connectar mqtt
  pinMode(PIN_TO_SENSOR, INPUT); //Segir að pin18 er input
}

void loop() {
  Serial.setTimeout(2000);
  pinState = digitalRead(PIN_TO_SENSOR);  // Les nýy value frá skynjara
  
  if (pinState == HIGH) {   // Ef skynjarinn er HIGH/skynjar hreyfingu
    Serial.println("Motion detected!");
    if(client.publish(bathroom_topic, "Motion detected")){ //Publishar á mqtt broker
      Serial.println("Motion sent!");
      }
     else{ //Ef hann náði ekki að senda reynir hann aftur
      Serial.println("Motion failed to send. Reconnecting to MQTT Broker and trying again"); 
      client.connect(clientID, mqtt_username, mqtt_password); //Connectar upp á nýtt
      delay(10);
      client.publish(bathroom_topic, "Motion detected"); //Sendir aftur á MQTT broker
      }
  }
  else
  if (pinState == LOW) { //Ef skynjarinn er LOW/engin hreyfing
    Serial.println("Motion stopped!");
    if(client.publish(bathroom_topic, "Motion Stopped")){ //Publishar motion stopped á MQTT Broker 
      Serial.println("Motion sent!");
      }
     else{ //Ef hann náði ekki að senda reynir hann aftur
      Serial.println("Motion failed to send. Reconnecting to MQTT Broker and trying again"); 
      client.connect(clientID, mqtt_username, mqtt_password); //Connectar upp á nýtt
      delay(10);
      client.publish(bathroom_topic, "Motion Stopped"); //Publishar upp á nýtt
      }
  }
  
  //client.disconnect();  // disconnect from the MQTT broker
  Serial.println(""); 
  delay(8000);       // Sendir nýtt value á 8 sekúndna fresti
}
