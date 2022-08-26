# Super simple garage door opener using a Pico W


I live in an apartment with a detached garage where the only entrance is through the garage door, and if you forget the remote in the garage, you are locked out. This was my solution for WiFi enabled garage door opener with these conditions and no WiFi within reach of the garage. This sits in my apartment about 200ft from my garage, and still able to trigger it.

My finished product.
![soldered pcb](/documents/soldered_pcb_beadboard.png)



# Parts
* $6 [Raspberry Pico W](https://www.canakit.com/raspberry-pi-pico-w.html)
* $13 [Cheap Garage Remote](https://www.amazon.com/dp/B08RSDQKM9?psc=1&ref=ppx_yo2ov_dt_b_product_details)
* Perfectly okay to leave in a breadboard, but I decided to solder to this [PCB](https://www.amazon.com/dp/B07ZYNWJ1S?psc=1&ref=ppx_yo2ov_dt_b_product_details) to make it a bit more permanent. But note you will need headers soldered to the pico to be able to plug a micro USB into the pico. If I had to do it over, I'd use this [PCB](https://shop.pimoroni.com/products/pico-proto-pcb?variant=39795939737683) made for Pico and solder directly to the PCB.
* 1 10k ohm resistor. It may not be needed, but I did not want much voltage going to the garage door opener if not be required.

# Wiring Diagram
![soldered pcb](/documents/Breadboard_Sketch_bb.png)

# Hardware Setup
* For the garage door remote, you can take it apart by two small Phillips head screws on the back.
* Once open, I'd hold it with the buttons on the bottom facing you. Then you solder your GPIO pin to the top lead left from the button to the PCB. Then solder your ground to the bottom left lead. If you buy a different remote, you can use a piece of wire to connect the two; if it lights up, then that's where it should be wired. You can also use a volt to find what is needed. What I did initially.
* Setup the remote for your garage motor following directions included with the remote. I'd solder the wires in and test that you can trigger a button press before setting up the remote with your garage to cut down on how many times it opens and close
* Wire up as seen in the diagram.


# Software Setup
You will find a [settings.json.example](settings.json.example). This file holds all the settings for this project.
Remove the `.example` so the file becomes `settings.json`, then enter your values.
* ssid - Your WiFi name
* ssid_password - Your WiFi password
* password - A clear-text password is needed to open your garage (100% not the most secure, just a bit of a determent if you are port forwarding to your pico).


1. Download and set up MicroPython. If not already can find out [here](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html).
2. Copy [main.py](main.py) and [settings.json](settings.json) to your Pico. (Can use [rshell](https://github.com/dhylands/rshell#cp) or [Throny](https://www.freva.com/transfer-files-between-computer-and-raspberry-pi-pico/) for this)
3. Using REPL for the pico should print the IP address. Use that and type `http://{pico-ip}/garage/toggle/{password-from-settings}` should see a web page and the pico light flash meaning it toggled GPIO Pin 14 to open the garage door. I set opening this URL to a shortcut on my iPhone to trigger the door. 