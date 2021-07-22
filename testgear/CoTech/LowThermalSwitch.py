# Low Thermal Mux

import testgear.base_classes as base

class LowThermalSwitch(base.instrument):
    def init(self):
        self.resource.baud_rate = 9600
    
    def default_VISA(self):
        return 'ASRL/dev/ttyUSB0::INSTR'

    def channel(self, channel=1):
        '''select input channel
        0 - short
        1 - Channel 1
        2 - Channel 2
        3 - open'''
        return self.query("{0}".format(channel))

    def short(self):
        '''Short output to the instrument to measure offset'''
        self.query("0")

    def open(self):
        '''open output to the instrument
        all channels are switched off'''
        self.query("2")