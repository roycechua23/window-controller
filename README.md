# window-controller
This project can control a window to automatically turn on / turn off via water sensor, temperature sensor, and manual control through mqtt and a Flask web application. The window will be controlled by the ESP8266 uploaded with MicroPython code and the MQTT broker as well as the Flask web application is hosted on the Raspberry Pi 3.

## Hardware Components
* ESP8266 (flashed with MicroPython firmware but you can also do it with Arduino Code)
* Rasbperry Pi 3 (Serves as the MQTT broker and hosts the Web Application for manual control)
* Rain Sensor
* DHT22 Temperature Sensor
* Stepper Motor / DC Motor

## Software Requirements
* Mosquitto 
* paho-mqtt (for Python)
* Flask

The codes were based on the tutorial of Rui Santos but modified for the project requirements (Micropython code for ESP8266, using DHT22, Rain Sensor, and the Stepper Motor). Refer to the link below.
https://randomnerdtutorials.com/raspberry-pi-publishing-mqtt-messages-to-esp8266/
