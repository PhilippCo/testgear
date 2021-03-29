"""Fluke 5450A Resistance Calibrator"""

import testgear.base_classes as base

class F5450A(base.calibrator):
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


    def set_value(self, value=None, open=False):
        """set output voltage"""
        if open:
            self.write("OPEN;")
        else:    
            self.write("OUTPUT {0:d};".format(value))
        return self.get_value()


    def get_value(self):
        """get actual output value"""
        return float(self.query("VALUE;"))


    def get_function(self):
        return 'OHMS'


    def get_functions(self):
        return ['OHMS']
    