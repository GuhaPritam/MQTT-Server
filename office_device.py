import json
import time
import paho.mqtt.client as mqtt
from config import Server


def on_connect(client, userdata, flag, rc):
    client.subscribe(Server.SUBSCRIBE_TOPIC)


def on_message(client, userdata, message):
    print("[ message ]", message.payload.decode())


def on_publish(client, userdata, result):
    print("[ publish ] Data is published")


def main():
    mqtt_client = mqtt.Client("send_data123", clean_session=True)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(host=Server.HOSTNAME, port=Server.PORT)
    mqtt_client.loop_start()

    while True:
        cmd = int(input("\n1) Turn ON Light\n2)Turn OFF Light\n3)Exit\nEnter your option :"))
        if cmd == 1:
            mqtt_client.publish(Server.PUBLISH_TOPIC, "light_on")
        elif cmd == 2:
            mqtt_client.publish(Server.PUBLISH_TOPIC, "light_off")
        else:
            break
    mqtt_client.loop_stop()


if __name__ == "__main__":
    main()
