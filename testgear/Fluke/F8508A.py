"""Fluke 8508A 8.5 digit DMM"""

import testgear.base_classes as base

class F8508A(base.meter):
    def init(self):
        pass

    def get_reading(self, channel=None):
        self.__select_channel(channel)
        return float(self.query("RDG?"))


    def __select_channel(self, channel):
        #to be done
        pass


    def conf_function_DCV(self, mrange=1000, nplc=200, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        pass


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