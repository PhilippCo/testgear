"""Fluke 8588A 8.5 digit DMM"""

import testgear.base_classes as base

class F8588A(base.meter):
    def init(self):
        self.idstr = self.query("*IDN?").strip()
        self.set_timeout(30)


    def get_reading(self, channel=None):
        #self.__select_channel(channel)
        return float(self.query("READ?"))


    def conf_function_DCV(self, mrange=1000, nplc=500, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__select_channel(channel)
        self.__conf_range("VOLT:DC", mrange, nplc)
        if HiZ:
            self.write(":SENSE:VOLT:DC:IMPedance AUTO")
        else:
            self.write(":SENSE:VOLT:DC:IMPedance 10M")


    def conf_function_DCI(self, mrange=None, nplc=500, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCI. if range=None the meter is set to Autorange"""
        self.__select_channel(channel)
        self.__conf_range("CURR:DC", mrange, nplc)


    def conf_function_ACV(self, mrange=None, nplc=500, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__select_channel(channel)
        self.__conf_range("VOLT:AC", mrange, nplc)


    def conf_function_ACI(self, mrange=None, nplc=500, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__select_channel(channel)
        self.__conf_range("CURR:AC", mrange, nplc)
  

    def conf_function_OHM2W(self, mrange=None, nplc=500, AutoZero=True, OffsetCompensation=False, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__select_channel(channel)
        self.__conf_range("RES", mrange, nplc)
        #Offset Compensation only supported on 4W mode


    def conf_function_OHM4W(self, mrange=None, nplc=500, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure 4w resistance. if range=None the meter is set to Autorange"""
        self.__select_channel(channel)
        
        if OffsetCompensation and mrange < 19.9e3:
            self.write(":SENSE:FRES:MODE TRUE") #True Ohms
        else:
            self.write(":SENSE:FRES:MODE NORM")
        
        self.__conf_range("FRES", mrange, nplc)
        

    def __select_channel(self, channel):
        if channel is None:
            return 0

        if channel == 2:
            self.select_terminal("REAR")
        else:
            self.select_terminal("FRONT")
        return 1


    def select_terminal(self, terminal="FRONT"):
        """select terminal for measurement FRONT or REAR"""
        self.write(":ROUTe:Terminals {0}".format(terminal))


    def __conf_range(self, prefix:str, mrange, nplc):
        self.write(':SENS:FUNC "{0:s}"'.format(prefix))
        self.write(":SENSE:{0:s}:RES MIN".format(prefix))
        
        if mrange is None:
            self.write(":SENS:{0:s}:RANGE:AUTO ON".format(prefix))
        else:
            self.write(":SENSE:{0:s}:RANGE {1:0.6g}".format(prefix, mrange))

        self.__set_nplc(prefix, nplc)


    def __set_nplc(self, prefix:str, nplc):
        self.write(":SENSE:{0:s}:NPLC {1:d}".format(prefix, nplc))
