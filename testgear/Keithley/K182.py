import testgear.base_classes as base

# K182.write("P0X") #digital Filters off   needed?
# K182.write("O0X") #analog Filters off   needed?
# K182.write("N0X") #all Filters off
# K182.write("S2X") #100ms integration time


class K182(base.dmm):
    def init(self):
        self.write("L1X") #reset instrument
        self.write("B1X") #6.5 digit mode
        self.write("F0X") #reading souce last readig from ADC
        self.write("G0X") #return reading only
        self.write("P0X") #digital Filters off   needed?
        self.write("O0X") #analog Filters off   needed?
        self.write("N0X") #all Filters off
        self.write("S2X") #100ms integration time


    def set_range(self, value=None, autorange=False):
        if autorange:
            self.write("R0X")
        else:
            if value <= 3e-3:
                self.write("R1X") #set 3mV range
            elif value <= 30e-3:
                self.write("R2X") #set 30mV Range
            elif value <= 300e-3:
                self.write("R3X") #set 300mV Range
            elif value <= 3:
                self.write("R4X") #set 3V Range
            else:
                self.write("R5X") #set 30V Range


    def get_reading(self):
        return float(self.read())
