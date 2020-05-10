# BeewiPy

<img src="https://img.shields.io/pypi/v/BeewiPy.svg" alt="latest release" /> <img src="https://img.shields.io/pypi/l/BeewiPy.svg" alt="license" />

A python library to interact with Beewi SmartBulb.

SmartBulb is a series of Smart LED color bulbs manufactured by Beewi. These bulbs are controlled using BTLE (Bluetooth Low Energy) and the vendor provides an Android app to interact with the bulbs.

This library has been tested with BeeWi BBL229.

## Getting started
Soon there will be a documentation section but meanwhile you can start here.
### Prerequisites
* Any linux distribution
* [Python 3](https://www.python.org/downloads/) - this library requires the use of Python 3.
* [BluePy](https://github.com/IanHarvey/bluepy) - this library relies on BluePy library made by [IanHarvey](https://github.com/IanHarvey).

### Installation
To install this library you can do it using `pip install BeewiPy`
### Scanning for your device
First of all you need to know the MAC address of your device, so start by getting this information. It can be done using several ways, the easiest one is looking it up on the app provided by BeeWi.
### Minimal working code
```python
from BeewiPy import *
import time

MAC_ADDRESS = "00:00:00:00:00:00"       # Here you should put the MAC address of your device
myBulb = BeewiSmartBulb(MAC_ADDRESS)    # This will create a new BeewiSmartBulb object and connect to the device
myBulb.turnOn()                         # This will turn on your bulb
time.sleep(5)                           # This will wait 5 seconds
myBulb.turnOff()                        # This will turn off your bulb
```
## The BeewiSmartBulb class
Every object instantiated from the BeewiSmartBulb class will have the following methods available:
### turnOn()
This method turns on the bulb
### turnOff()
This method turns off the bulb
### setBrightness(value)
This method will set the brightness value of the bulb. The accepted values range from 0 to 9.
### setTemperature(value)
This method will set the temperature value of the bulb. The accepted values range from 0 to 9, being 0 the coolest setting and 9 the warmest setting.
### setColor(red, green, blue)
This method will change the color of the bulb. The values passed for red, green and blue must be between 0 and 255.
### setWhite()
This method will change the bulb from color mode to white mode.
### setColorSequence(value)
This method will put the bulb in color sequence mode. In this mode the color of the bulb will cycle in predefined sequences. The value passed to this function range from 0 to 4.

## Authors
* **David Polo**
## License
This project is licensed under the GNU General Public License v.3
## Acknowledgements
* Special thanks to [IanHarvey](https://github.com/IanHarvey) for its [BluePy](https://github.com/IanHarvey/bluepy) library.
