"""Fluke 5440B Voltage Calibrator"""

import testgear.base_classes as base

class F5440B(base.calibrator):

    def set_output(self, voltage=None, current=None, enabled=True):
        """set output. current isn't supported"""
        self.output(enabled)
        self.set_value(voltage)


    def output(self, state):
        if state:
            self.write("OPER")
        else:
            self.write("STBY")

    def guard(self, state):
        """Guard configuration:
            True -> Guard connected to LO
            False -> Guard disconnected from LO
        """
        if state:
            self.write("IGRD")
        else:
            self.write("EGRD")


    def div(self, state):
        """Divider configuration:
            True -> Output divided
            False -> Output not divided
        """
        if state:
            self.write("DIVY")
        else:
            self.write("DIVN")


    def external_sense(self, state):
        """4W configuration:
            True -> external sense (4W)
            False -> internal sense (2W)
        """
        if state:
            self.write("ESNS")
        else:
            self.write("ISNS")


    def set_value(self, value):
        """set output voltage"""
        self.write("SOUT {0:0.8g}; OPER".format(value))


    def get_value(self):
        """get actual output value"""
        return float(self.query("GOUT"))


    def get_function(self):
        return 'VDC'


    def get_functions(self):
        return ['VDC']
    