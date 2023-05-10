import paho.mqtt.client as mqtt
import queue

COMMANDS = queue.Queue()

PUB_TOPIC = "/api/blaze"
SUB_TOPIC = "/api/minipc"


def on_connect(client, userdata, flags, rc):
    print("[ info ] connected")


def on_message(client, userdata, message):
    global COMMANDS
    cmd = message.payload.decode()
    print("[ message ] ", cmd)
    COMMANDS.put(cmd)


def on_publish(client, userdata, result):  # create function for callback
    print("[ publish ] Data is Published")


def main():
    # def on_log(client,userdata, flags, rc):
    mqtt_client = mqtt.Client("received_data123", clean_session=True)
    # mqtt_client.on_log = on_log
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(host='tenxertech.local', port=1883)
    mqtt_client.subscribe(SUB_TOPIC)
    mqtt_client.loop_start()
    while True:
        if COMMANDS.qsize():
            cmd = COMMANDS.get()
            print("CMD :", cmd)
            if cmd == "light_on":
                print("light is on")


if __name__ == "__main__":
    main()
