
import testgear.base_classes as base

class HP3458A(base.meter):
    def init(self):
        self.write("END ALWAYS")
        self.write("NDIG 8")

        if "HP3458A" not in self.query("ID?"):
            print("no HP3458A detected!!")
            return 1

        self.set_timeout(30)


    def default_VISA(self):
        return 'TCPIP::192.168.2.88::gpib0,22::INSTR'


    def get_reading(self):
        return float(self.read())


    def display(self, text):
        self.write("DISP MSG {0:s}".format(text))


    def __set_range(self, range, NPLC):
        if range is None:
            self.write("RANGE AUTO")
        else:
            self.write("RANGE {0:0.6f}".format(range))

        self.write("NPLC {0:0.3f}".format(NPLC))


    def __autoZero(self, enabled=True):
        if enabled:
            self.write("AZERO ON")
        else:
            self.write("AZERO OFF")


    def __hiZ(self, enabled=True):
        if enabled:
            self.write("FIXEDZ OFF")
        else:
            self.write("FIXEDZ ON")

  
    def conf_function_DCV(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.write("DCV")
        self.__set_range(mrange, nplc)
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_DCI(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCI. if range=None the meter is set to Autorange"""
        self.write("DCI")
        self.__set_range(mrange, nplc)
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_ACV(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.write("ACV")
        self.__set_range(mrange, nplc)
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_ACI(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.write("ACI")
        self.__set_range(mrange, nplc)
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_OHM2W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.write("ACV")
        self.__set_range(mrange, nplc)
        self.__autoZero(AutoZero)


    def conf_function_OHM4W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.write("ACV")
        self.__set_range(mrange, nplc)
        self.__autoZero(AutoZero)
