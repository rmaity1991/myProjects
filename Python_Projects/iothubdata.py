from azure.iot.device import Message
from azure.iot.device.aio import IoTHubDeviceClient
import numpy as np

connection_string='HostName=dfr-rht-iothub.azure-devices.net;DeviceId=PTS-case1-evapTemperature;SharedAccessKey=3Sk1tDNxWN/90bFLfFi/HViW2UN1qYho8zkUU2FI/1A='

PAYLOAD = '{{"temperature": {temperature}}}'

client=IoTHubDeviceClient.create_from_connection_string(connection_string)


simulation_temperature_list=np.random.random(10)


for var in simulation_temperature_list:
    data = PAYLOAD.format(temperature=var)

    message = Message(data)
    print(message)
    print(f"Sending message: {message}")
    client.send_message(message)
    print("Message successfully sent")



client.shutdown()



