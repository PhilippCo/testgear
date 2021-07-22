# Low Thermal Mux

import testgear.base_classes as base

class LowThermalSwitch(base.instrument):
    def init(self):
        #hier die Serielle Schnittstelle konfigurieren. Baudrate etc.
        self.resource.baud_rate = 9600
    
    def default_VISA(self):
        return 'ASRL/dev/ttyUSB0::INSTR'

    def channel(self, channel=0):
        pass
