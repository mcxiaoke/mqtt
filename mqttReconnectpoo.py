import paho.mqtt.client as mqtt

# Create a client instance
client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Automatically subscribe to topics when connected
    client.subscribe("your/topic")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

# Assign event callbacks
client.on_connect = on_connect
client.on_disconnect = on_disconnect

# Configure automatic reconnection
client.reconnect_delay_set(min_delay=1, max_delay=120)

# Connect to the broker
client.connect("mqtt.broker.address", 1883, 60)

# Start the loop
client.loop_forever()
