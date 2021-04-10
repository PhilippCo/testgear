"""Fluke 5440B Voltage Calibrator"""

import testgear.base_classes as base

class F5440B(base.source):

    def set_output(self, voltage=None, current=None, enabled=True, frequency=None, resistance=None, channel=1):
        """set output. current isn't supported"""
        if enabled:
            self.write("OPER")
        else:
            self.write("STBY")

        if voltage is not None:
            self.write("SOUT {0:0.8g}; OPER".format(voltage))

    
    def get_output(self):
        """return an object which reflects the output conditions"""
        obj = base.output_status()

        obj.set_voltage = float(self.query("GOUT"))

        return obj


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

    