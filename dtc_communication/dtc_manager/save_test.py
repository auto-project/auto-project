import paho.mqtt.publish as publish
publish.single("/dtc", 'U0001', hostname='localhost')
