
import testgear.base_classes as base

# VISA String: 'ASRL/dev/ttyACM0::INSTR'


class KA3005P(base.pwrsupply):
    def set_output(self, voltage=None, current=None, enabled=True):
        if enabled:
            self.write("OUT1")
        else:
            self.write("OUT0")

        if voltage is not None:
            self.write("VSET1:{0:0.2f}".format(voltage))
        
        if current is not None:
            self.write("ISET1:{0:0.3f}".format(current))


    def get_status(self):
        data = self.query("STATUS?").strip()
        return int.from_bytes( bytes(data, "utf-8"), "big")


    def get_output(self):
        if self.get_status() & 0x40:
            enabled = True
        else:
            enabled = False

        voltage = float(self.query("VSET1?"))
        current = float(self.query("ISET1?"))
        return voltage, current, enabled


    def read_output(self):
        voltage = float(self.query("VOUT1?"))
        current = float(self.query("IOUT1?"))
        return voltage, current


    def over_voltage_protection(self, state=False):
        if state:
            self.write("OVP1")
        else:
            self.write("OVP0")


    def over_current_protection(self, state=False):
        if state:
            self.write("OCP1")
        else:
            self.write("OCP0")
