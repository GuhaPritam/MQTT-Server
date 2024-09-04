import json
import time
import paho.mqtt.client as mqtt
from config import Server
import queue

MQTT_DATA = queue.Queue()
global MQTT_CLIENT


def on_connect(client, userdata, flag, rc):
    client.subscribe(Server.OFFICE_SUB_TOPIC)


def on_message(client, userdata, message):
    global MQTT_DATA
    cmd = message.payload.decode()
    MQTT_DATA.put(cmd)


def on_publish(client, userdata, result):
    print("[ publish ] Data is published")


def send_data_to_home(command):
    MQTT_CLIENT.publish(Server.OFFICE_PUB_TOPIC, command)


def get_from_home(command):
    global MQTT_DATA
    __start_time = time.time()
    while time.time() - __start_time < 180:
        if MQTT_DATA:
            __start_time = time.time()
            if MQTT_DATA.qsize():
                data = MQTT_DATA.get()
                print("CMD : ", data)
                if data == command:
                    return data


def main():
    global MQTT_CLIENT
    MQTT_CLIENT = mqtt.Client("send_data123", clean_session=True)
    MQTT_CLIENT.on_connect = on_connect
    MQTT_CLIENT.on_message = on_message
    MQTT_CLIENT.connect(host=Server.HOSTNAME, port=Server.PORT)
    MQTT_CLIENT.loop_start()
    send_data_to_home("light_on")
    get_from_home("light_on_done")
    print("light is done")

    # while True:
    #     cmd = int(input("\n1) Turn ON Light\n2)Turn OFF Light\n3)Exit\nEnter your option :"))
    #     if cmd == 1:
    #         send_data_to_home("light_on")
    #     elif cmd == 2:
    #         send_data_to_home("light_off")
    #     else:
    #         break
    # MQTT_CLIENT.loop_stop()


if __name__ == "__main__":
    main()
