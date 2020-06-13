# DTC Forwarding team repository

## Base configuration

1. Installing RaspberryPi3B+ with Raspbian operating system using NOOBS.
2. Install MQTT and enable service
   * apt-get install mosquitto
   * systemctl start mosquitto
3. Confiugre Raspberry to connect to WiFi network.
4. "Open" ports on WiFi network:
    * port 22 - SSH for the team
    * port 1883 - MQTT port
    * port 8080 - HMI endpoint
5. Setup service to automatically start:
    * Communication for DTC raising
    * Communication between DTC forwarding and HMI


## Contents

* [Communication for DTC raising](dtc_communication)
* [Communication between DTC forwarding and HMI](DataController)
