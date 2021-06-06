"""Fluke 5730A Multifunction Calibrator"""

import testgear.base_classes as base

class F5730A(base.source):

    def init(self):
        idstring = self.query("*IDN?").split(",")
        if idstring[0] == "FLUKE" and idstring[1] == "5730A":
            print("Fluke 5730A calibrator detected")
        else:
            print("no Fluke 5730A detected!") #raise error?
        

    def set_output(self, voltage=None, current=None, enabled=True, frequency=None, resistance=None, channel=1):
        if enabled:
            # write("OUT 10V, 0Hz;*CLS;OPER")
            pass

        else: #not enabled
            self.write("STBY")

    
    def get_output(self):
        """return an object which reflects the output conditions"""
        obj = base.output_status()

        #add uncertainty absolute and in ppm

        return obj