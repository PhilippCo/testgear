import testgear.base_classes as base
import numpy as np

class HP3478A(base.meter):
    def init(self):
        self.idstr = ""

        self.set_timeout(30)


    def default_VISA(self):
        return 'TCPIP::192.168.2.88::gpib0,23::INSTR'


    def get_reading(self, channel=None):
        self.write("T3") #single Trigger
        return float(self.read().strip())


    def conf_function_DCV(self, mrange=None, nplc=10, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.write("F1") #DCV Function

        if mrange is None:
            self.write("RA")
        else:
            if mrange <= 30e-3:
                self.write("R-2") #set 30mV range
            elif mrange <= 300e-3:
                self.write("R-1") #set 300mV Range
            elif mrange <= 3:
                self.write("R0") #set 3V Range
            elif mrange <= 30:
                self.write("R1") #set 30V Range
            else:
                self.write("R2") #set 300V Range

        if nplc <= 0.1:
            self.write("N3") #NPLC 0.1
        elif nplc <= 1:
            self.write("N4") #NPLC 1
        else:
            self.write("N5") #NPLC 10 (10x1)

        if AutoZero:
            self.write("Z1")
        else:
            self.write("Z0")


    def conf_function_DCI(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCI. if range=None the meter is set to Autorange"""
        self.write("F5") #DCI Function

        if mrange is None:
            self.write("RA")
        else:
            if mrange <= 300e-3:
                self.write("R-1") #set 300mA range
            else:
                self.write("R0") #set 3A Range

        if nplc <= 0.1:
            self.write("N3") #NPLC 0.1
        elif nplc <= 1:
            self.write("N4") #NPLC 1
        else:
            self.write("N5") #NPLC 10 (10x1)

        if AutoZero:
            self.write("Z1")
        else:
            self.write("Z0")


    def conf_function_ACV(self, mrange=None, nplc=None, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure ACV. if range=None the meter is set to Autorange"""
        self.write("F2") #ACV Function

        if mrange is None:
            self.write("RA")
        else:
            if mrange <= 300e-3:
                self.write("R-1") #set 300mV Range
            elif mrange <= 3:
                self.write("R0") #set 3V Range
            elif mrange <= 30:
                self.write("R1") #set 30V Range
            else:
                self.write("R2") #set 300V Range

        if nplc <= 0.1:
            self.write("N3") #NPLC 0.1
        elif nplc <= 1:
            self.write("N4") #NPLC 1
        else:
            self.write("N5") #NPLC 10 (10x1)

        if AutoZero:
            self.write("Z1")
        else:
            self.write("Z0")



    def conf_function_ACI(self, mrange=None, nplc=None, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.write("F6") #ACI Function

        if mrange is None:
            self.write("RA")
        else:
            if mrange <= 300e-3:
                self.write("R-1") #set 300mA range
            else:
                self.write("R0") #set 3A Range

        if nplc <= 0.1:
            self.write("N3") #NPLC 0.1
        elif nplc <= 1:
            self.write("N4") #NPLC 1
        else:
            self.write("N5") #NPLC 10 (10x1)

        if AutoZero:
            self.write("Z1")
        else:
            self.write("Z0")


    def conf_function_OHM2W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.write("F3") #2W Ohm Function

        if mrange is None:
            self.write("RA")
        else:
            if mrange <= 30:
                self.write("R1") #set 30Ohm range (R1-R7)
            elif mrange <= 300:
                self.write("R2") #set 300Ohm range
            elif mrange <= 3000:
                self.write("R3") #set 3kOhm range
            elif mrange <= 30e3:
                self.write("R4") #set 30kOhm range
            elif mrange <= 300e3:
                self.write("R5") #set 300kOhm range
            elif mrange <= 3e6:
                self.write("R6") #set 3MOhm range
            else:
                self.write("R7") #set 30MOhm range

        if nplc <= 0.1:
            self.write("N3") #NPLC 0.1
        elif nplc <= 1:
            self.write("N4") #NPLC 1
        else:
            self.write("N5") #NPLC 10 (10x1)

        if AutoZero:
            self.write("Z1")
        else:
            self.write("Z0")


    def conf_function_OHM4W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.write("F4") #4W Ohm Function

        if mrange is None:
            self.write("RA")
        else:
            if mrange <= 30:
                self.write("R1") #set 30Ohm range (R1-R7)
            elif mrange <= 300:
                self.write("R2") #set 300Ohm range
            elif mrange <= 3000:
                self.write("R3") #set 3kOhm range
            elif mrange <= 30e3:
                self.write("R4") #set 30kOhm range
            elif mrange <= 300e3:
                self.write("R5") #set 300kOhm range
            elif mrange <= 3e6:
                self.write("R6") #set 3MOhm range
            else:
                self.write("R7") #set 30MOhm range

        if nplc <= 0.1:
            self.write("N3") #NPLC 0.1
        elif nplc <= 1:
            self.write("N4") #NPLC 1
        else:
            self.write("N5") #NPLC 10 (10x1)

        if AutoZero:
            self.write("Z1")
        else:
            self.write("Z0")
