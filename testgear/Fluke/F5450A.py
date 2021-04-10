"""Fluke 5450A Resistance Calibrator"""

import testgear.base_classes as base
import numpy as np

class F5450A(base.source):
    def reset(self):
        self.write("CLEAR;")


    def get_status(self):
        return self.query("STATUS;")


    def guard(self, state):
        """Guard configuration:
            True -> Guard connected to LO
            False -> Guard disconnected from LO
        """
        if state:
            self.write("EXT GUARD OFF;")
        else:
            self.write("EXT GUARD ON;")


    def set_output(self, resistance=None, voltage=None, current=None, enabled=True, frequency=None, channel=1):
        if not enabled:
            self.write("OPEN;")
        else:    
            self.write("OUTPUT {0:d};".format(resistance))

        self.get_output()
        
    
    def get_output(self, channel=1):
        """return an object which reflects the output conditions"""
        obj = base.output_status()

        obj.resistance = float(self.query("VALUE;"))

        if obj.resistance > 1e30:
            obj.enabled    = False
            obj.resistance = np.nan
        else:
            obj.enabled = True

        return obj
    