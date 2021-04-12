
import testgear.base_classes as base

class HP603xA(base.source):
    def set_output(self, voltage=None, current=None, enabled=True, frequency=None, resistance=None, channel=1):
        if enabled:
            self.write("OUT ON")
        else:
            self.write("OUT OFF")

        if voltage is not None:
            self.write("VSET {0:f}".format(voltage))

        if current is not None:
            self.write("ISET {0:f}".format(current))


    def get_output(self, channel=1):
        """return an object which reflects the output conditions"""
        obj = base.output_status()

        obj.set_voltage = float(self.query("VSET?")[4:].strip())
        obj.set_current = float(self.query("ISET?")[4:].strip())

        obj.voltage = float(self.query("VOUT?")[4:].strip())
        obj.current = float(self.query("IOUT?")[4:].strip())

        if self.query("OUT?").strip() == "OUT 1":
            obj.enabled = True
        else:
            obj.enabled = False

        return obj


