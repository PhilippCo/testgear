"""Fluke 8508A 8.5 digit DMM"""

import testgear.base_classes as base

class F8508A(base.meter):
    def init(self):
        pass

    def get_reading(self, channel=None):
        self.__select_channel(channel)
        return float(self.query("X?"))


    def __select_channel(self, channel):
        #to be done
        pass


    def conf_function_DCV(self, mrange=1000, nplc=200, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.write("DCV {0:0.3f}".format(mrange))
        self.write("DCV RESL 7")
        self.write("DCV FAST_OFF")


    def conf_function_DCI(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCI. if range=None the meter is set to Autorange"""
        pass


    def conf_function_ACV(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        pass


    def conf_function_ACI(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        pass


    def conf_function_OHM2W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        pass


    def conf_function_OHM4W(self, mrange=None, nplc=200, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure 4w resistance. if range=None the meter is set to Autorange"""
        pass

#if float(r) <= 2:
#    self.visa.write("TRUE_OHMS 1.9")
#    self.visa.write("TRUE_OHMS FAST_OFF")
#    self.visa.write("TRUE_OHMS RESL7")

#elif float(r) <= 20:
#    self.visa.write("TRUE_OHMS 19")
#    self.visa.write("TRUE_OHMS FAST_OFF")
#    self.visa.write("TRUE_OHMS RESL7")
    
#elif float(r) <= 200:
#    self.visa.write("TRUE_OHMS 190")
#    self.visa.write("TRUE_OHMS FAST_OFF")
#    self.visa.write("TRUE_OHMS RESL7")

#elif float(r) <= 2e3:
#    self.visa.write("TRUE_OHMS 1900")
#    self.visa.write("TRUE_OHMS FAST_OFF")
#    self.visa.write("TRUE_OHMS RESL7")

#elif float(r) <= 20e3:
#    self.visa.write("TRUE_OHMS 19000")
#    self.visa.write("TRUE_OHMS FAST_OFF")
#    self.visa.write("TRUE_OHMS RESL7")

#elif float(r) <= 200e3:
#    self.visa.write("OHMS 190e3")
#    self.visa.write("OHMS FOUR_WR")
#    self.visa.write("OHMS FAST_OFF")
#    self.visa.write("OHMS RESL7")

#elif float(r) <= 2e6:
#    self.visa.write("OHMS 1.9e6")
#    self.visa.write("OHMS FOUR_WR")
#    self.visa.write("OHMS FAST_OFF")
#    self.visa.write("OHMS RESL7")
    
#elif float(r) <= 20e6:
#    self.visa.write("OHMS 19e6")
#    self.visa.write("OHMS FOUR_WR")
#    self.visa.write("OHMS FAST_OFF")
#    self.visa.write("OHMS RESL7")

#else:
#    self.visa.write("OHMS 190e6")
#    self.visa.write("OHMS FOUR_WR")
#    self.visa.write("OHMS FAST_OFF")
#    self.visa.write("OHMS RESL7")
