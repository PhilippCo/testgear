
import testgear.base_classes as base

class A6632B(base.source):
    def set_output(self, voltage=None, current=None, enabled=True):
        if enabled:
            self.write("OUTP ON")
        else:
            self.write("OUTP OFF")

        if voltage is not None:
            self.set_voltage(voltage)

        if current is not None:
            self.set_current(current)


    def set_voltage(self, value):
        self.write("VOLT {0:f}".format(value))

    def set_current(self, value):
        self.write("CURR {0:f}".format(value))

    def get_act_voltage(self):
        return float(self.query("MEASure:VOLTage?"))

    def get_act_current(self):
        return float(self.query("MEASure:CURRent?"))

    def get_set_voltage(self):
        return float(self.query("VOLTage?"))

    def get_set_current(self):
        return float(self.query("CURRent?"))
