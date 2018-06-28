# Ceed
The Ceed is a Raspberry Pi-based project for the frontrunners of the green energy transition to use to help motivate others to take action to save the planet.

![alt text](https://github.com/jakeh999/Ceed/blob/master/outside_view.jpg "Outside vide of the Ceed")

# Components
## Technical
* Raspberry Pi 3
* 1 Tiny Breadboard
* [Raspberry Pi 10.1-Inch-1366x768 Display Kit](https://wiki.52pi.com/index.php/10.1-Inch-1366x768_Display_Kit(without_Touch_Screen)_SKU:Z-0114)
* 6 volt 2100 mA DC plug for screen
* Some electrical wiring and a switch
* HDMI cable
* 1 HC-SR04 Ultrasonic Sensor
* [6x 16mm Pushbuttons](http://adafru.it/1504)
* Connection wires
* 4 mm MDF board
![alt text](https://github.com/jakeh999/Ceed/blob/master/Ceed_Schematic.jpg "Technical Schematic")

## Software
* Raspbian OS April 2018 with all updates installed
* Compiled Python 3.6 with gpiozero and omxplayer Python modules installed from pip3.6
* Compiled latest version of OMXplayer - https://github.com/popcornmix/omxplayer

# Assembly
Use a laser cutter to cut the MDF according to the Ceed Design file. It may be necessary to change the size of the switch port to match your own. Then use some strong glue to put the sides together, leaving the top part seperate. Next, use 2 hinges and screws to connect the top part to the bottom. Use some of the remaining glue to mount the sensor in place. After that, install the wiring, buttons, screen, LCD controller and screen switch, and Raspberry Pi. The switch should be used to control the power of the Raspberry Pi, since the screen needs to be on first so that the Pi activates its HDMI port. Once the system is up and running, install the software and test the Python script. Once everything works, setup a cronjob to automatically run the script on startup. Done!

![alt text](https://github.com/jakeh999/Ceed/blob/master/top_view.jpg "Top view of box")
![alt text](https://github.com/jakeh999/Ceed/blob/master/bottom_view.jpg "Bottom view of box")
