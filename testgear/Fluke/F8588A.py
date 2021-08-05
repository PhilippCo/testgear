"""Fluke 8588A 8.5 digit DMM"""

import testgear.base_classes as base

class F8588A(base.meter):
    def init(self):
        self.idstr = self.query("*IDN?").strip()


    def get_reading(self):
        return float(self.query("READ?"))


    def conf_function_DCV(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        pass


    def conf_function_DCI(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCI. if range=None the meter is set to Autorange"""
        pass


    def conf_function_ACV(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        pass


    def conf_function_ACI(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        pass


    def conf_function_OHM2W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        pass


    def conf_function_OHM4W(self, mrange=None, nplc=200, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure 4w resistance. if range=None the meter is set to Autorange"""
        self.__select_chanel(channel)
        self.write(':SENS:FUNC "FRES"') #select 4w ohms
        self.write(":SENSE:FRES:RANGE 1") #1 Ohm Range
        self.write(":SENSE:FRES:NPLC 200") #200NPLC
        self.write(":SENSE:FRES:MODE TRUE") #True Ohms
        self.write(":SENSE:FRES:RES 8") #8.5 digits


    def __select_channel(self, channel):
        if channel == 2:
            self.select_terminal("REAR")
        else:
            self.select_terminal("FRONT")


    def select_terminal(self, terminal="FRONT"):
        """select terminal for measurement FRONT or REAR"""
        self.write(":ROUTe:Terminals {0}".format(terminal))

#inst.query(":SENSE:FRES:RANGE?")
