# HP34401A 6.5 digit DMM

import testgear.base_classes as base

class HP34401A(base.meter):
    def init(self):
        self.set_timeout(10)
        self.idstr = self.query("*IDN?").strip()


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
        
        #  FUNCtion "FREQuency"
        #  FUNCtion "PERiod"
        #  FUNCtion "CONTinuity"
        #  FUNCtion "DIODe"
        #  FUNCtion "VOLTage:DC:RATio"

        # use aperture as gatetime
        # FREQuency:APERture {0.01|0.1|1|MINimum|MAXimum}
        # Select the aperture time (or gate time) for frequency measurements (the default
        # is 0.1 seconds). Specify 10 ms (41⁄2 digits), 100 ms (default; 51⁄2 digits), or
        # 1 second (61⁄2 digits). MIN = 0.01 seconds. MAX = 1 second.


    def conf_function_DCV(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__conf_range("VOLT:DC", mrange)
        self.write("VOLT:DC:NPLC {0:0.3f}".format(nplc))
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_DCI(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCI. if range=None the meter is set to Autorange"""
        self.__conf_range("CURR:DC", mrange)
        self.write("CURR:DC:NPLC {0:0.3f}".format(nplc))
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_ACV(self, mrange=None, nplc=None, AutoZero=True, HiZ=True, filter=3, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__conf_range("VOLT:AC", mrange)
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)

        #AC Filter Bandwitch can be 3Hz, 20Hz, 200Hz
        self.write("SENSe:DETector:BANDwidth {0:d}".format(filter))


    def conf_function_ACI(self, mrange=None, nplc=None, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__conf_range("CURR:AC", mrange)
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_OHM2W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__conf_range("RES", mrange)
        self.write("RES:NPLC {0:0.3f}".format(nplc))
        

    def conf_function_OHM4W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__conf_range("FRES", mrange)
        self.write("FRES:NPLC {0:0.3f}".format(nplc))