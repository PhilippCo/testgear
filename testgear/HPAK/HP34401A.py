# HP34401A 6.5 digit DMM

import testgear.base_classes as base

class HP34401A(base.meter):
    def init(self):
        self.set_timeout(10)


    def default_VISA(self):
        return 'TCPIP::192.168.2.88::gpib0,4::INSTR'


    def __autoZero(self, enabled):
        if enabled:
            self.write("ZERO:AUTO ON")
        else:
            self.write("ZERO:AUTO OFF")


    def __hiZ(self, enabled):
        if enabled:
            self.write("INPUT:IMPEDANCE:AUTO ON")
        else:
            self.write("INPUT:IMPEDANCE:AUTO OFF")


    def get_reading(self, channel=1):
        return float(self.query("READ?"))


    def __conf_range(self, prefix:str, range):
        self.write("CONF:{0:s}".format(prefix))
        
        if range is None:
            self.write("{0:s}:RANGE:AUTO ON".format(prefix))
        else:
            self.write("{0:s}:RANGE {1:0.6f}".format(prefix, range))
        

    def conf_function_DCV(self, range=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__conf_range("VOLT:DC", range)
        self.write("VOLT:DC:NPLC {0:0.3f}".format(nplc))
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_DCI(self, range=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCI. if range=None the meter is set to Autorange"""
        self.__conf_range("CURR:DC", range)
        self.write("CURR:DC:NPLC {0:0.3f}".format(nplc))
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_ACV(self, range=None, nplc=None, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__conf_range("VOLT:AC", range)
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_ACI(self, range=None, nplc=None, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__conf_range("CURR:AC", range)
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_OHM2W(self, range=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__conf_range("RES", range)
        self.write("RES:NPLC {0:0.3f}".format(nplc))
        

    def conf_function_OHM4W(self, range=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__conf_range("FRES", range)
        self.write("FRES:NPLC {0:0.3f}".format(nplc))