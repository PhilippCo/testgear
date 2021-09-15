"""Fluke 8508A 8.5 digit DMM"""

import testgear.base_classes as base

class F8508A(base.meter):
    def init(self):
        self.set_timeout(180)
        self.__guard()
        self.idstr = self.query("*IDN?").strip()
        self.write("TRG_SRCE EXT") #no internal trigger


    def get_reading(self, channel=None):
        return float(self.query("X?")) #X? is equal to *TRG;RDG?


    def select_terminal(self, terminal="FRONT"):
        """select terminal for measurement FRONT, REAR or OFF"""
        self.write("INPUT {0}".format(terminal))


    def __guard(self, guard=True):
        self.write("GUARD INT") #default on power on
        #self.write("GUARD EXT")


    def conf_function_DCV(self, mrange=None, nplc=200, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        if mrange is None:
            self.write("DCV AUTO")
        else:    
            self.write("DCV {0:0.3f}".format(mrange))

        self.write("DCV RESL7")
        self.write("DCV FAST_OFF")
        self.write("DCV TWO_WR")
        self.write("DCV FILT_OFF")


    def conf_function_DCI(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCI. if range=None the meter is set to Autorange"""
        if mrange is None:
            self.write("DCI AUTO")
        else:    
            self.write("DCI {0:0.3f}".format(mrange))

        self.write("DCI RESL7") #7 Digits is maximum for current
        self.write("DCI FAST_OFF")
        self.write("DCI FILT_OFF")


    def conf_function_ACV(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        if mrange is None:
            self.write("ACV AUTO")
        else:    
            self.write("ACV {0:0.3f}".format(mrange))
        
        self.write("ACV RESL6") #6 Digits is maximum for ACV
        self.write("ACV TWO_WR")
        self.write("ACV TFER_ON")
        self.write("ACV FILT40HZ")
        #self.write("ACV DCCP") #DC coupled
        self.write("ACV ACCP") #AC coupled


    def conf_function_ACI(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        if mrange is None:
            self.write("ACI AUTO")
        else:    
            self.write("ACI {0:0.3f}".format(mrange))

        self.write("ACI RESL6") #6 Digits is maximum for ACI
        self.write("ACI FILT40HZ")
        self.write("ACI FILT40HZ")
        #self.write("ACI DCCP") #DC coupled
        self.write("ACI ACCP") #AC coupled


    def conf_function_OHM2W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=False, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        if mrange is None:
            self.write("OHMS AUTO")
        else:    
            self.write("OHMS {0:0.3f}".format(mrange))

        self.write("OHMS RESL7")
        self.write("OHMS FAST_OFF")
        self.write("OHMS TWO_WR")
        self.write("OHMS LOI_OFF")
        self.write("OHMS FILT_OFF")


    def conf_function_OHM4W(self, mrange=None, nplc=200, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure 4w resistance. if range=None the meter is set to Autorange"""
        if not OffsetCompensation and mrange < 20e3: #True Ohms only up to 20kOhm
            if mrange is None:
                self.write("OHMS AUTO")
            else:    
                self.write("OHMS {0:0.3f}".format(mrange))

            self.write("OHMS RESL7")
            self.write("OHMS FAST_OFF")
            self.write("OHMS FOUR_WR")
            self.write("OHMS LOI_OFF")
            self.write("OHMS FILT_OFF")

        else:
            if mrange is None:
                self.write("TRUE_OHMS AUTO")
            else:    
                self.write("TRUE_OHMS {0:0.3f}".format(mrange))

            self.write("TRUE_OHMS RESL7")
            self.write("TRUE_OHMS FAST_OFF")
            self.write("TRUE_OHMS FOUR_WR")
            self.write("TRUE_OHMS LOI_OFF")
            self.write("TRUE_OHMS FILT_OFF")


    def conf_function_HV_OHM2W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=False, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        if mrange is None:
            self.write("HIV_OHMS AUTO")
        else:    
            self.write("HIV_OHMS {0:0.3f}".format(mrange))

        self.write("HIV_OHMS RESL7")
        self.write("HIV_OHMS FAST_OFF")
        self.write("HIV_OHMS TWO_WR")
        self.write("HIV_OHMS LOI_OFF")
        self.write("HIV_OHMS FILT_OFF")


    def conf_function_HV_OHM4W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=False, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        if mrange is None:
            self.write("HIV_OHMS AUTO")
        else:    
            self.write("HIV_OHMS {0:0.3f}".format(mrange))

        self.write("HIV_OHMS RESL7")
        self.write("HIV_OHMS FAST_OFF")
        self.write("HIV_OHMS FOUR_WR")
        self.write("HIV_OHMS LOI_OFF")
        self.write("HIV_OHMS FILT_OFF")

