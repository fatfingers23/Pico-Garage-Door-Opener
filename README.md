## Super simple garage door opener using a Pico W

Documentation is still a wip

Things to add to documentation
* Garage door opener used, along with pic of the solder
* Pin lay out diagram


### Settings
You will find a [settings.json.example](settings.json.example), this file holds all the swettings for this project.
Remove the `.example` so the file becomes `settings.json`, then enter in your values.
* ssid - Your WiFi name
* ssid_password - Your WiFi password
* password - A clear text password needed to open your garage (100% not the most secure, just a bit of a determent if you are port forwarding to your pico).


### Software Setup
1. Download and setup MicroPython. If not already can find out [here](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html).
2. Copy [main.py](main.py) and [settings.json](settings.json) to your Pico. (Can use [rshell](https://github.com/dhylands/rshell#cp) or [Throny](https://www.freva.com/transfer-files-between-computer-and-raspberry-pi-pico/) for this)
3. Using REPL for the pico should print the ip address. Use that and type `http://{pico-ip}/garage/toggle/{passowrd-from-settings}` should see a web page and the pico light flash meaning it toggled GPIO Pin 14 to open the garage door


### Hardware Setup
1. WIP