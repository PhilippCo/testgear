
import testgear.base_classes as base

# VISA String: 

class KA3005P(base.source):
    def init(self):
        pass

    def default_VISA(self):
        #return 'ASRL/dev/ttyACM0::INSTR' #local connection on USB
        return "TCPIP::192.168.2.87::korad1::INSTR" #connection via RPi

    def set_output(self, voltage=None, current=None, enabled=True, frequency=None, resistance=None, channel=1):
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

    def get_output(self, channel=1):
        """return an object which reflects the output conditions"""
        obj = base.output_status()

        if self.get_status() & 0x40:
            obj.enabled = True
        else:
            obj.enabled = False

        obj.set_voltage = float(self.query("VSET1?"))
        obj.set_current = float(self.query("ISET1?"))
        
        obj.voltage = float(self.query("VOUT1?"))
        obj.current = float(self.query("IOUT1?"))
        return obj

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

    def store_config(self, memory):
        self.write("SAV{0:d}".format(memory))

    def load_config(self, memory):
        self.write("RCL{0:d}".format(memory))