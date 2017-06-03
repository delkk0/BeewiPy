#!/usr/bin/python3
from bluepy.btle import * # Import bluetoothctl library
import time


class BeewiSmartBulb:
    TURN_ON  = bytes([85,16, 1,13,10])
    TURN_OFF = bytes([85,16, 0,13,10])
    SET_BRIGHTNESS =   [bytes([85,18, 2,13,10]),
                        bytes([85,18, 3,13,10]),
                        bytes([85,18, 4,13,10]),
                        bytes([85,18, 5,13,10]),
                        bytes([85,18, 6,13,10]),
                        bytes([85,18, 7,13,10]),
                        bytes([85,18, 8,13,10]),
                        bytes([85,18, 9,13,10]),
                        bytes([85,18,10,13,10]),
                        bytes([85,18,11,13,10])]
    SET_TEMPERATURE =  [bytes([85,17, 2,13,10]),
                        bytes([85,17, 3,13,10]),
                        bytes([85,17, 4,13,10]),
                        bytes([85,17, 5,13,10]),
                        bytes([85,17, 6,13,10]),
                        bytes([85,17, 7,13,10]),
                        bytes([85,17, 8,13,10]),
                        bytes([85,17, 9,13,10]),
                        bytes([85,17,10,13,10]),
                        bytes([85,17,11,13,10])]
    SET_WHITE = bytes([85,20,255,255,255,13,10])
    SET_COLOR = bytearray([85,19,255,255,255,13,10])
    SET_COLOR_SEQUENCE = [bytes([85,23, 8,13,10]),
                          bytes([85,23, 9,13,10]),
                          bytes([85,23,10,13,10]),
                          bytes([85,23,11,13,10]),
                          bytes([85,23,12,13,10])]

    CHARACTERISTIC_SMARTLITE_SETTINGS = "a8b3fff1-4834-4051-89d0-3de95cddd318"
    CHARACTERISTIC_SMARTLITE_READ_SETTINGS = "a8b3fff2-4834-4051-89d0-3de95cddd318"

    def __init__(self, deviceAddress):
        self.deviceAddress = deviceAddress
        self.bulb = Peripheral()
        self.bulb.connect(self.deviceAddress)
        self.writeSettingCharacteristic = self.bulb.getCharacteristics(uuid=BeewiSmartBulb.CHARACTERISTIC_SMARTLITE_SETTINGS)[0]
        self.readSettingCharacteristic = self.bulb.getCharacteristics(uuid=BeewiSmartBulb.CHARACTERISTIC_SMARTLITE_READ_SETTINGS)[0]
        if (0x22 <= self.readSettings()[1] <= 0xBB):
            self.isWhite = 1
        elif (self.readSettings()[1] == 0xB0):
            self.isWhite = 0

        if (self.readSettings()[1] == 0x01):
            self.isOn = 1
        elif (self.readSettings()[1] == 0x00):
            self.isOn = 0

    def writeSettings(self, command):
        return self.writeSettingCharacteristic.write(command)

    def readSettings(self):
        return self.readSettingCharacteristic.read()

    def turnOn(self):
        self.writeSettings(BeewiSmartBulb.TURN_ON)
        self.isOn = 1

    def turnOff(self):
        self.writeSettings(BeewiSmartBulb.TURN_OFF)
        self.isOn = 0

    def setBrightness(self, brightness):
        if(brightness > 9 or brightness < 0):
            print("Brightness should be a value between 0 and 9")
            return 1
        self.writeSettings(BeewiSmartBulb.SET_BRIGHTNESS[brightness])

    def setTemperature(self, temperature):
        if(temperature > 9 or temperature < 0):
            print("Temperature should be a value between 0 and 9")
            return 1
        self.writeSettings(BeewiSmartBulb.SET_TEMPERATURE[temperature])

    def setWhite(self):
        if(not self.isWhite):
            self.writeSettings(BeewiSmartBulb.SET_WHITE)
            self.isWhite = 1

    def setColor(self, red, green, blue):
        if(0 <= red <= 255) and (0 <= green <= 255) and (0 <= blue <= 255):
            self.isWhite = 0
            self.SET_COLOR[2] = red
            self.SET_COLOR[3] = green
            self.SET_COLOR[4] = blue

            self.writeSettings(self.SET_COLOR)

    def setColorSequence(self, sequence):
        if (0 <= sequence <= 4):
            self.isWhite = 0
            self.writeSettings(BeewiSmartBulb.SET_COLOR_SEQUENCE[sequence])
        else:
            print ("Sequence must be a number from 0 to 4")

    def __del__(self):
        self.bulb.disconnect()
