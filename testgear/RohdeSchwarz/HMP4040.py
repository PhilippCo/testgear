
import testgear.base_classes as base

class HMP4040(base.source):
    def set_output(self, voltage=None, current=None, enabled=True, resistance=None, frequency=None, channel=1):
        self.write("INST OUT{:d}".format(channel))

        if enabled:
            self.write("OUTP:STAT 1")
        else:
            self.write("OUTP:STAT 0")

        if voltage is not None:
            self.write("VOLT {0:f}".format(voltage))

        if current is not None:
            self.write("CURR {0:f}".format(current))


    def get_output(self, channel=1):
        self.write("INST OUT{:d}".format(channel))
        """return an object which reflects the output conditions"""
        obj = base.output_status()

        obj.set_voltage = float(self.query("VOLTage?"))
        obj.set_current = float(self.query("CURRent?"))

        obj.voltage = float(self.query("MEASure:VOLTage?"))
        obj.current = float(self.query("MEASure:CURRent?"))

        if self.query("OUTP:STAT?").strip() == "1":
            obj.enabled = True
        else:
            obj.enabled = False

        return obj