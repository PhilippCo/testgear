"""Valhalla 2703 AC voltage calibrator"""

import testgear.base_classes as base

class V2703(base.source):
    def init(self):
        self.write("E4") #EOI asserted with last character
        self.set_voltage = self.get_output().set_voltage


    def set_output(self, voltage=None, current=None, enabled=True, frequency=None, resistance=None, channel=1):
        if enabled:
            if voltage is not None:
                self.write("V{0:0.7g}".format(voltage))
            else:
                self.write("V{0:0.7g}".format(self.set_voltage)) #if voltage isn't specified restore saved one

            self.set_voltage = self.get_output().set_voltage #update stored set_voltage

        else:
            self.write("V0.0")

        if frequency is not None:
            self.write("F{0:0.7g}".format(frequency))


    def get_output(self):
        """return an object which refelcts the output conditions"""
        obj = base.output_status()

        status = self.query("E").strip().split(",")

        obj.set_voltage   = float(status[0])
        obj.frequency = float(status[1]) * 1e3
        obj.waveform  = "SINE"

        if obj.set_voltage == 0:
            obj.enabled     = False
            obj.set_voltage = self.set_voltage
        else:
            obj.enabled = True

        return obj


    def external_sense(self, state):
        """4W configuration:
            True -> external sense (4W)
            False -> internal sense (2W)
        """
        if state:
            self.write("S1")
        else:
            self.write("S0")
