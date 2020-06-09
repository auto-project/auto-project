# DTC library python wrapper

## Description and functionality

The functionality of the `dtc_manager` is to listen for DTCs using MQTT and then 
persist them on the server running it using the `diaglib` library provided by the 
DTC team. 

This project takes the diaglib files (`cpp` and `hpp`) and using `SWIG` and an 
interface tailored for our needs (`diaglib.i`) and a custom `setup.py` file, 
creates an extension python module `dtc_lib.py` and an accompanying `_dtc_lib.so` 
file containing the shared object that the module will direct the calls to.

The python module is then used in the python project `dtc_controller` and through
the exposed methods in it, it routes the requests to the `_dtc_lib.so` file.

## Setup MQTT communication for raised DTCs

1. Use the `dtc_lib_build_tools/swigsetup.sh` script to build and setup the needed 
extension module for the dtc_manager. 
    * It will require you to have `SWIG` installed.
        ```shell script
        sudo apt-get install swig
        ```
    * Also paho-mqtt is needed for the communication.
        ```shell script
        pip3 install paho-mqtt
        ```
2. After setting up the library, the communication is started from the `communication.py` file.
```shell script
python3 communication.py
```

## Information for clients

All that clients need to do in order to raise a DTC is to contact the server 
that is hosting the communication with the string containing the DTC in question.
An example file has been added in this repository containing an example request 
towards the ip that, as of writing this documentation, is the host of the communication.
It's pretty simple, here's a snippet:

```python
import paho.mqtt.publish as publish
publish.single("/dtc", 'U0001', hostname='localhost')
```

One important thing to note is that the DTCs are in the following format: 
**One leading capital letter followed by 4 digits**. For a full specification you'd 
have to contact the DTC team.
