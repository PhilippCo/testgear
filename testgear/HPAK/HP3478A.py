import testgear.base_classes as base
import numpy as np

class HP3478A(base.meter):
    def init(self):
        self.idstr = self.query("ID?").strip()

        self.set_timeout(30)


    def default_VISA(self):
        return 'TCPIP::192.168.2.88::gpib0,23::INSTR'


    def get_reading(self, channel=None):
        return float(self.read().strip())
