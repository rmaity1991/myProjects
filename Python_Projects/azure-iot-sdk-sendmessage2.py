import os
import asyncio
import uuid
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message

messages_to_send = 10



# Connection string should never be stored in code, but for simplicity we are using it.
connection_str = "Insert your Connection String"

# The client object is used to interact with your Azure IoT hub.
device_client = IoTHubDeviceClient.create_from_connection_string(connection_str)

# Connect the client.
device_client.connect()



for i in range(5):
    msg=Message(f"Hello World , I am the {i} message")
    print("Sending Message {} ".format(i))
    device_client.send_message(msg)

# Finally, shut down the client
device_client.shutdown()
