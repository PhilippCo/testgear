
import testgear.base_classes as base

class Almemo1030(base.source):
    def init(self):
        self.resource.baud_rate = 9600
    
    def default_VISA(self):
        return 'ASRL/dev/serial/by-id/usb-Silicon_Labs_ALMEMO_to_USB_11091439-if00-port0::INSTR'

    def get_temp(self):
        self.write("p")
        self.resource.read_raw()
        data = self.resource.read_raw()
        self.resource.read_raw()

        return float(str(data)[6:-10])
    
    def set_output(self, voltage, current, enabled, frequency, resistance, fourWire, channel):
        pass
    
    def get_output(self):
        pass
