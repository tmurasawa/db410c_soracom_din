#!/usr/bin/python
import time

from gpio_96boards import GPIO
import paho.mqtt.client as mqtt

# GPIO_A is D_A on Mezzanine
GPIO_A = GPIO.gpio_id('GPIO_A')
pins = (
    (GPIO_A, 'in'),
)

def on_connect(client, userdata, rc):
  print("Connected with result code " + str(rc))
  #if you use Scalenics WITHOUT SORACOM,comment out below..
  #client.subscribe("<DEVICE_TOKEN>/<DEVICE_ID>/subscribe")
  #if you use Scalenics WITH SORACOM,comment out below..
  client.subscribe(topic)

def on_disconnect(client, userdata, rc):
  if rc != 0:
     print("Unexpected disconnection.")

def on_publish(client, userdata, mid):
  print("publish: {0}".format(mid))


def tilt(gpio):
    while True:
			pin_current = False
			pin_stat = gpio.digital_read(GPIO_A)
			#print "GPIO_A:%s" %pin_stat
			if pin_stat == 0:
				cnt += 1
			else:
				cnt = 0
			if cnt == 20:
				pin_current = not(pin_current)

			if pin_current:
				print "Push!"
				print "Published topic:%s" %topic
				# send ON
				client.publish(topic, "v=1")
				time.sleep(0.1)
				# send OFF
				client.publish(topic, "v=0")


print "-- Get metadata from SORACOM..."


import json
import requests

metadata=requests.get('http://metadata.soracom.io/v1/subscriber').json()
#print metadata
imsi=metadata["imsi"]
print "imsi:%s" %imsi

device_token=requests.get('http://metadata.soracom.io/v1/userdata').text
print "device_token:%s" %device_token

topic = device_token
print "MQTT topic:%s" %topic


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Blink LED on GPIO A (pin 23)')
    args = parser.parse_args()

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    #client.on_message = on_message

		## if you use Scalenics WITHOUT SORACOM,comment out below..
		#client.username_pw_set("<SCALENICS_ID>","<DEVICE_TOKEN>")
		#client.connect("api.scalenics.io", 1883, 10)
		## if you use Scalenics WITH SORACOM,comment out below..
    client.connect("beam.soracom.io", 1883, 10)

    with GPIO(pins) as gpio:
        tilt(gpio)

