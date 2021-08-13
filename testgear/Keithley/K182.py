import testgear.base_classes as base

class K182(base.meter):
    def init(self):
        self.write("L1X") #reset instrument
        self.write("B1X") #6.5 digit mode
        self.write("F0X") #reading souce last readig from ADC
        self.write("G0X") #return reading only
        self.write("P0X") #digital Filters off   needed?
        self.write("O0X") #analog Filters off   needed?
        self.write("N0X") #all Filters off
        self.write("S2X") #100ms integration time -> NPLC 5


    def conf_function_DCV(self, mrange=1000, nplc=5, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""

        #NLPC is fixed to 5
        if mrange is None:
            self.write("R0X")
        else:
            if mrange <= 3e-3:
                self.write("R1X") #set 3mV range
            elif mrange <= 30e-3:
                self.write("R2X") #set 30mV Range
            elif mrange <= 300e-3:
                self.write("R3X") #set 300mV Range
            elif mrange <= 3:
                self.write("R4X") #set 3V Range
            else:
                self.write("R5X") #set 30V Range


    def get_reading(self, channel=1):
        return float(self.read())
