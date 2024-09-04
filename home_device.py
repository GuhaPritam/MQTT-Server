import paho.mqtt.client as mqtt
import queue
from config import Server

MQTT_DATA = queue.Queue()


def on_connect(client, userdata, flag, rc):
    print("[ info ] Connected")
    client.subscribe(Server.HOME_SUB_TOPIC)


def on_message(client, userdata, message):
    global MQTT_DATA
    cmd = message.payload.decode()
    print("[ message ]", cmd)
    MQTT_DATA.put(cmd)


def on_publish(client, userdata, result):
    print("[ publish ] Data is published")


def main():
    mqtt_client = mqtt.Client("receive_data123", clean_session=True)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(host=Server.HOSTNAME, port=Server.PORT)
    mqtt_client.loop_start()

    while True:
        if MQTT_DATA.qsize():
            cmd = MQTT_DATA.get()
            print("CMD :", cmd)
            if cmd == "light_on":
                print("Light is on")
                mqtt_client.publish(Server.HOME_PUB_TOPIC, "light_on_done")


if __name__ == "__main__":
    main()
