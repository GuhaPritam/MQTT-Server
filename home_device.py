import paho.mqtt.client as mqtt
import queue

mqtt_data = queue.Queue()

PUB_TOP = '/home/device'
SUB_TOP = '/office/device'


def on_connect(client, userdata, flag, rc):
    print("[ info ] Connected")


def on_message(client, userdata, message):
    global mqtt_data
    cmd = message.payload.decode()
    print("[ message ]", cmd)
    mqtt_data.put(cmd)


def on_publish(client, userdata, result):
    print("[ publish ] Data is published")


def main():
    mqtt_client = mqtt.Client("receive_data123", clean_session=True)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(host='localhost', port=1883)
    mqtt_client.subscribe(SUB_TOP)
    mqtt_client.loop_start()

    while True:
        if mqtt_data.qsize():
            cmd = mqtt_data.get()
            print("CMD :", cmd)
            # if cmd == "light_on":
            #     print("Light is on")


if __name__ == "__main__":
    main()
