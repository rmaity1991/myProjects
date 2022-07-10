import os
import asyncio
import uuid
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message
import random

messages_to_send = 10


async def main():
    # The connection string for a device should never be stored in code. For the sake of simplicity we're using an environment variable here.
    conn_str = 'HostName=rht-dfr-iothub.azure-devices.net;DeviceId=dfr-rht-device1;SharedAccessKey=CqPY8HaqoxyZJsmuPrEWzHguQJQOanEBhMCWIvhjji0='

    # The client object is used to interact with your Azure IoT hub.
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Connect the client.
    await device_client.connect()

    async def send_test_message(i):
        msg = Message("This is a Random Number " + str(random.randint(10,30)))
        await device_client.send_message(msg)
        print("done sending message #" + str(i))

    # send `messages_to_send` messages in parallel
    await asyncio.gather(*[send_test_message(i) for i in range(1, 20)])

    # Finally, shut down the client
    await device_client.shutdown()


if __name__ == "__main__":
    asyncio.run(main())