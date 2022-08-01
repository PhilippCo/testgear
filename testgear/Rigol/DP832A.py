import testgear.base_classes as base
import numpy as np
import time

class DP832A(base.source):
    def init(self):
        self.idstr = self.query("*IDN?").strip()


    def default_VISA(self):
        return 'USB0::6833::3601::DP8B163050514::0::INSTR'


    def set_output(self, voltage=None, current=None, enabled=True, resistance=None, frequency=None, channel=1):
        self.write(":APPLy CH{:d}".format(channel))

        if enabled:
            self.write("OUTP:STAT ON")
        else:
            self.write("OUTP:STAT OFF")

        if voltage is not None:
            self.write("VOLT {0:f}".format(voltage))

        if current is not None:
            self.write("CURR {0:f}".format(current))


    def get_output(self, channel=1):
        """return an object which reflects the output conditions"""

        self.write(":APPLy CH{:d}".format(channel))
        
        obj = base.output_status()
        obj.channel = channel

        obj.set_voltage = float(self.query("VOLTage?"))
        obj.set_current = float(self.query("CURRent?"))

        obj.voltage = float(self.query("MEASure:VOLTage?"))
        obj.current = float(self.query("MEASure:CURRent?"))

        if self.query("OUTP:STAT?").strip() == "1":
            obj.enabled = True
        else:
            obj.enabled = False

        return obj