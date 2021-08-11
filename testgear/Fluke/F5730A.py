"""Fluke 5730A Multifunction Calibrator"""

import testgear.base_classes as base

class F5730A(base.source):

    def init(self):
        self.idstr = self.query("*IDN?").strip()

        idstring = self.idstr.split(",")
        if idstring[0] == "FLUKE" and idstring[1] == "5730A":
            print("Fluke 5730A calibrator detected")
        else:
            print("no Fluke 5730A detected!") #raise error?
        

    def set_output(self, voltage=None, current=None, enabled=True, frequency=0, resistance=None, fourWire=False, channel=1):
        if enabled:

            if voltage is not None:
                unit  = "V"
                value = voltage
            elif current is not None:
                unit  = "A"
                value = current
            elif resistance is not None:
                unit  = "OHM"
                value = resistance
                frequency = 0

            self.write("OUT {0:0.6g}{1}, {2:0.6g}Hz;*CLS;OPER".format(value, unit, frequency))

        else: #not enabled
            self.write("STBY")

    
    def get_output(self):
        """return an object which reflects the output conditions"""
        obj = base.output_status()

        #add uncertainty absolute and in ppm

        return obj