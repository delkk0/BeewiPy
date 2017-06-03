# BeewiPy
A python library to interact with Beewi SmartBulb.

SmartBulb is a series of Smart LED color bulbs manufactured by Beewi. These bulbs are controlled using BTLE (Bluetooth Low Energy) and the vendor provides an Android app to interact with the bulbs.

This library has been tested with BeeWi BBL229.

**This is still work in progress! Today I have tested some of the methods, but not all and not using all the possible combinations. Any suggestion to improve the code is very welcome!**

## Getting started
Soon there will be a documentation section but meanwhile you can start here.
### Prerequisites
* Any linux distribution
* [Python 3](https://www.python.org/downloads/) - this library requires the use of Python 3.
* [BluePy](https://github.com/IanHarvey/bluepy) - this library relies on BluePy library made by [IanHarvey](https://github.com/IanHarvey).

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
### The sky is the limit!

## Authors
* **David Polo**
## License
This project is licensed under the GNU General Public License v.3
## Acknowledgements
* Special thanks to [IanHarvey](https://github.com/IanHarvey) for its [BluePy](https://github.com/IanHarvey/bluepy) library.
