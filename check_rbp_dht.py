#!/usr/bin/python

from pynagios import Plugin, make_option
import sys
import Adafruit_DHT

class DHT(Plugin):
    devicetype = make_option("-d","--device", dest="devicetype", type="int")
    pin = make_option("-p","--pin", dest="pin", type="int")
    mode = make_option("-t","--type", dest="mode", type="string", help="temp|hum")
    unit = make_option("-u","--unit", dest="unit", type="string", help="c|f")

    def check(self):

        sensor = self.options.devicetype
        pin = self.options.pin
        unit = self.options.unit

        #read from DHT
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        #generate output
        if mode == 'temp':
            value = temperature
            if unit == 'c':
                temperature = temperature * 1.8 + 32
                output = 'Temperature is {0:0.1f}*F'.format(temperature)
        elif unit == 'hum':
            value = humidity
            output = 'Humidity is {0:0.1f}%'.format(humidity)
        else:
            print "You shoudn't be here"
        #return response
        result = self.response_for_value(value, message=output)
        result.set_perf_data("Value", value,warn=self.options.warning,crit=self.options.critical)
        return result

if __name__ == '__main__':
    DHT().check().exit()