
import testgear.base_classes as base

class Almemo1030(base.source):
    def init(self):
        self.resource.baud_rate = 9600
    
    def default_VISA(self):
        return 'ASRL/dev/ttyUSB0::INSTR'

    def get_temp(self):
        self.write("p")
        self.resource.read_raw()
        data = self.resource.read_raw()
        self.resource.read_raw()

        data = self.query("p")
        return float(str(data)[6:-10])
