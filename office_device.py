import json
import time
import paho.mqtt.client as mqtt

SUB_TOP = '/home/device'
PUB_TOP = '/office/device'


def on_connect(client, userdata, flag, rc):
    client.subscribe(SUB_TOP)


def on_message(client, userdata, message):
    print("[ message ]", message.payload.decode())


def on_publish(client, userdata, result):
    print("[ publish ] Data is published")


def main():
    mqtt_client = mqtt.Client("send_data123", clean_session=True)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(host='localhost', port=1883)
    mqtt_client.loop_start()

    while True:
        cmd = int(input("\n1) Turn ON Light\n2)Turn OFF Light\n3)Exit\nEnter your option :"))
        if cmd == 1:
            mqtt_client.publish(PUB_TOP, "light_on")
        elif cmd == 2:
            mqtt_client.publish(PUB_TOP, "light_off")
        else:
            break
    mqtt_client.loop_stop()


if __name__ == "__main__":
    main()
