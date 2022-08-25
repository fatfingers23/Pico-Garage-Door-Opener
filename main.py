import ujson
import utime
import network
from machine import Pin
import uasyncio as asyncio

"""
Settings setup
"""
json_settings = open('settings.json')
settings = ujson.load(json_settings)
json_settings.close()

ssid = settings['ssid']
password = settings['ssid_password']
garage_password = settings['password']

html = """<!DOCTYPE html>
<html>
    <head> <Title>Garage Door Opener</Title></head>
    <body>
        <h1>Pico W Home Page</h1>
        <p>%s</p>
    </body> 

</html>"""

"""
Pin set ups
"""
software_button = Pin(14, Pin.OUT, Pin.PULL_UP)
software_button.value(1)
onboard_led = Pin('LED', Pin.OUT)
button = Pin(12, Pin.IN, Pin.PULL_DOWN)

"""
Wifi setup
"""


def connect_to_network():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    max_wait = 10

    # Wait for connect or fail 12 max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
    max_wait -= 1
    print('waiting for connection...')
    utime.sleep(1)

    # Handle connection error
    if wlan.status() != 3:
        onboard_led.toggle()
        utime.sleep(2)
        onboard_led.toggle()
        utime.sleep(2)
        onboard_led.toggle()
        utime.sleep(2)
        raise RuntimeError('network connection failed')
    else:
        onboard_led.toggle()
        utime.sleep(2)
        onboard_led.toggle()
        utime.sleep(2)
        print('connected')
        status = wlan.ifconfig()
        print('ip = ' + status[0])


def toggle_garage():
    software_button.value(0)
    utime.sleep(.1)
    software_button.value(1)


async def serve_client(reader, writer):
    print("Client connected")
    onboard_led.on()
    request_line = await reader.readline()
    print("Request:", request_line)
    # We are not interested in HTTP request headers, skip them
    while await reader.readline() != b"\r\n":
        pass
    request = str(request_line)
    toggle_door = request.find('/garage/toggle/' + password)
    stateis = ""
    if toggle_door == 6:
        print("Toggling door")
        toggle_garage()
        stateis = "Toggled"
    response = html % stateis
    writer.write('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    writer.write(response)
    await writer.drain()
    await writer.wait_closed()
    print("Client disconnected")
    onboard_led.off()


async def main():
    onboard_led.on()
    connect_to_network()

    print("Setting up webserver...")
    asyncio.create_task(asyncio.start_server(serve_client, "0.0.0.0", 80))
    onboard_led.off()
    while True:
        print("hearbeat")
        await asyncio.sleep(0.25)
        await asyncio.sleep(5)


try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()
