"""Agilent B2902A Precision Source/Measure Unit"""

import testgear.base_classes as base
import numpy as np

class B2902A(base.source):
    def init(self):
        self.set_timeout(10)
        self.idstr = self.query("*IDN?").strip()

    
    def set_output(self, voltage=10, current=10e-3, enabled=True, frequency=None, resistance=None, mode="voltage", channel=1):
        if enabled:
            self.write(":OUTP{0:d} ON".format(channel))
        else:
            self.write(":OUTP{0:d} OFF".format(channel))

            
        if mode == "current":
            self.write(":SOUR{0:d}:FUNC:MODE CURR".format(channel))
            self.write(":SENS{0:d}:VOLT:PROT {1:0.7f}".format(channel, voltage))
            self.write(":SOUR{0:d}:CURR {1:0.7f}".format(channel, current))
            
        else: #voltage mode
            self.write(":SOUR{0:d}:FUNC:MODE CURR".format(channel))
            self.write(":SENS{0:d}:CURR:PROT {1:0.7f}".format(channel, current))
            self.write(":SOUR{0:d}:VOLT {1:0.7f}".format(channel, voltage))


    def get_output(self, channel=1):
        """return an object which reflects the output conditions"""
        obj = base.output_status()
        obj.channel = channel

        if self.query(":OUTP{0:d}?".format(channel)).strip() == "1":
            obj.enabled = True

            obj.set_voltage = float(self.query(":SOUR{0:d}:VOLT?".format(channel)).strip())
            obj.set_current = float(self.query(":SOUR{0:d}:CURR?".format(channel)).strip())

            obj.voltage = float(self.query(":MEAS:VOLT? (@{0:d})".format(channel)).strip())
            obj.current = float(self.query(":MEAS:CURR? (@{0:d})".format(channel)).strip())
            
        else:
            obj.enabled = False
        
        return obj

