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

    SERVICE_SMARTLITE_CONTROL = "a8b3fff0-4834-4051-89d0-3de95cddd318"

    CHARACTERISTIC_SMARTLITE_SETTINGS = "a8b3fff1-4834-4051-89d0-3de95cddd318"
    CHARACTERISTIC_SMARTLITE_READ_SETTINGS = "a8b3fff2-4834-4051-89d0-3de95cddd318"

    SERVICE_SMARTLITE_DEVICE_INFORMATION = "0000180a-0000-1000-8000-00805f9b34fb"
    CHARACTERISTIC_SYSTEM_ID = "00002a23-0000-1000-8000-00805f9b34fb"
    CHARACTERISTIC_MODEL_NUMBER_STRING = "00002a24-0000-1000-8000-00805f9b34fb"
    CHARACTERISTIC_FIRMWARE_REVISION_STRING = "00002a26-0000-1000-8000-00805f9b34fb"
    CHARACTERISTIC_HARDWARE_REVISION_STRING = "00002a27-0000-1000-8000-00805f9b34fb"
    CHARACTERISTIC_SOFTWARE_REVISION_STRING = "00002a28-0000-1000-8000-00805f9b34fb"
    CHARACTERISTIC_MANUFACTURER_NAME_STRING = "00002a29-0000-1000-8000-00805f9b34fb"

    def __init__(self, deviceAddress):
        self.deviceAddress = deviceAddress
        self.bulb = Peripheral()
        self.bulb.connect(self.deviceAddress)
<<<<<<< HEAD
        self.serviceControl = self.bulb.getServiceByUUID(BeewiSmartBulb.SERVICE_SMARTLITE_CONTROL)
        self.serviceInformartion = self.bulb.getServiceByUUID(BeewiSmartBulb.SERVICE_SMARTLITE_DEVICE_INFORMATION)

        self.writeSettingCharacteristic = self.serviceControl.getCharacteristics(forUUID=BeewiSmartBulb.CHARACTERISTIC_SMARTLITE_SETTINGS)[0]
        self.readSettingCharacteristic = self.bulb.getCharacteristics(forUUID=BeewiSmartBulb.CHARACTERISTIC_SMARTLITE_READ_SETTINGS)[0]

=======
        self.writeSettingCharacteristic = self.bulb.getCharacteristics(endHnd = 0x003f, uuid=BeewiSmartBulb.CHARACTERISTIC_SMARTLITE_SETTINGS)[0]
        self.readSettingCharacteristic = self.bulb.getCharacteristics(endHnd = 0x003f, uuid=BeewiSmartBulb.CHARACTERISTIC_SMARTLITE_READ_SETTINGS)[0]
>>>>>>> b22bc0c6cd5c54bc04a0c74e94b3ed7b8daf1cf4
        if (0x22 <= self.__readSettings()[1] <= 0xBB):
            self.isWhite = 1
        elif (self.__readSettings()[1] == 0xB0):
            self.isWhite = 0
        if (self.__readSettings()[1] == 0x01):
            self.isOn = 1
        elif (self.__readSettings()[1] == 0x00):
            self.isOn = 0

    def __writeSettings(self, command):
        return self.writeSettingCharacteristic.write(command)

    def __readSettings(self):
        self.settings = self.readSettingCharacteristic.read()
        self.isOn = self.settings[0]
        if(0x22 <= self.settings[1] <= 0xBB):
            self.isWhite = 1
            self.temperature = (self.settings[1] & 0x0F) - 2
        elif(0x20 <= self.settings[1] <= 0xB0):
            self.isWhite = 0
        self.brightness = ((self.settings[1] & 0xF0) >> 4) - 2
        self.red = self.settings[2]
        self.green = self.settings[3]
        self.blue = self.settings[4]

        return self.settings

    def turnOn(self):
        self.__readSettings()
        self.__writeSettings(BeewiSmartBulb.TURN_ON)
        self.isOn = 1

    def turnOff(self):
        self.__readSettings()
        self.__writeSettings(BeewiSmartBulb.TURN_OFF)
        self.isOn = 0

    def setBrightness(self, brightness):
        self.__readSettings()
        if(brightness > 9 or brightness < 0):
            print("Brightness should be a value between 0 and 9")
            return 1
        self.__writeSettings(BeewiSmartBulb.SET_BRIGHTNESS[brightness])

    def setTemperature(self, temperature):
        self.__readSettings()
        if(temperature > 9 or temperature < 0):
            print("Temperature should be a value between 0 and 9")
            return 1
        self.__writeSettings(BeewiSmartBulb.SET_TEMPERATURE[temperature])

    def setWhite(self):
        self.__readSettings()
        if(not self.isWhite):
            self.__writeSettings(BeewiSmartBulb.SET_WHITE)
            self.isWhite = 1

    def setColor(self, red, green, blue):
        self.__readSettings()
        if(0 <= red <= 255) and (0 <= green <= 255) and (0 <= blue <= 255):
            self.isWhite = 0
            self.SET_COLOR[2] = red
            self.SET_COLOR[3] = green
            self.SET_COLOR[4] = blue

            self.__writeSettings(self.SET_COLOR)

    def setColorSequence(self, sequence):
        self.__readSettings()
        if (0 <= sequence <= 4):
            self.isWhite = 0
            self.__writeSettings(BeewiSmartBulb.SET_COLOR_SEQUENCE[sequence])
        else:
            print ("Sequence must be a number from 0 to 4")

    def getSettings(self, verbose = 0):
        self.__readSettings()
        if verbose:
            print("       ON/OFF : {}".format(self.isOn))
            print("  WHITE/COLOR : {}".format(self.isWhite))
            print("   BRIGHTNESS : {}".format(self.brightness))
            print("  TEMPERATURE : {}".format(self.temperature))
            print("COLOR (R/G/B) : {} {} {}".format(self.red, self.green, self.blue))

        return self.settings

    def getHWInfo(self):
<<<<<<< HEAD
        macAddress = self.serviceInformartion.getCharacteristics(forUUID=BeewiSmartBulb.CHARACTERISTIC_SYSTEM_ID)[0].read()
        modelNumberString = self.serviceInformartion.getCharacteristics(forUUID=BeewiSmartBulb.CHARACTERISTIC_MODEL_NUMBER_STRING)[0].read().decode('utf-8')[:-1]
        fwRevisionString = self.serviceInformartion.getCharacteristics(forUUID=BeewiSmartBulb.CHARACTERISTIC_FIRMWARE_REVISION_STRING)[0].read().decode('utf-8')[:-1]
        hwRevisionString = self.serviceInformartion.getCharacteristics(forUUID=BeewiSmartBulb.CHARACTERISTIC_HARDWARE_REVISION_STRING)[0].read().decode('utf-8')[:-1]
        manufacturerName = self.serviceInformartion.getCharacteristics(forUUID=BeewiSmartBulb.CHARACTERISTIC_MANUFACTURER_NAME_STRING)[0].read().decode('utf-8')[:-1]
=======
        macAddress = self.bulb.getCharacteristics(endHnd = 0x003f, uuid=BeewiSmartBulb.CHARACTERISTIC_SYSTEM_ID)[0].read()
        modelNumberString = self.bulb.getCharacteristics(endHnd = 0x003f, uuid=BeewiSmartBulb.CHARACTERISTIC_MODEL_NUMBER_STRING)[0].read().decode('utf-8')[:-1]
        fwRevisionString = self.bulb.getCharacteristics(endHnd = 0x003f, uuid=BeewiSmartBulb.CHARACTERISTIC_FIRMWARE_REVISION_STRING)[0].read().decode('utf-8')[:-1]
        hwRevisionString = self.bulb.getCharacteristics(endHnd = 0x003f, uuid=BeewiSmartBulb.CHARACTERISTIC_HARDWARE_REVISION_STRING)[0].read().decode('utf-8')[:-1]
        manufacturerName = self.bulb.getCharacteristics(endHnd = 0x003f, uuid=BeewiSmartBulb.CHARACTERISTIC_MANUFACTURER_NAME_STRING)[0].read().decode('utf-8')[:-1]
>>>>>>> b22bc0c6cd5c54bc04a0c74e94b3ed7b8daf1cf4

        print("MAC Address:       {:02X}:{:02X}:{:02X}:{:02X}:{:02X}:{:02X}".format(macAddress[7], macAddress[6], macAddress[5], macAddress[2], macAddress[1], macAddress[0]))
        print("Model number:      {}".format(modelNumberString))
        print("Firmware revision: {}".format(fwRevisionString))
        print("Hardware revision: {}".format(hwRevisionString))
        print("Manufacturer name: {}".format(manufacturerName))

    def __del__(self):
        self.bulb.disconnect()
