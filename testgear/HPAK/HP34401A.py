# HP34401A 6.5 digit DMM

import testgear.base_classes as base

class HP34401A(base.meter):
    
    spec_1year = { 
        'DCV': { 
            120e-3: {'mrange': 100e-3, 'reading': 0.0050, 'range': 0.0035},
            1.2   : {'mrange': 1     , 'reading': 0.0040, 'range': 0.0007},
            12    : {'mrange': 10    , 'reading': 0.0035, 'range': 0.0005},
            120   : {'mrange': 100   , 'reading': 0.0045, 'range': 0.0006},
            1000  : {'mrange': 1000  , 'reading': 0.0045, 'range': 0.0010}
        },
        
        'ACV': {
            100e-3: { 5    : {'mrange': 100e-3, 'reading': 1.00, 'range': 0.04},
                      10   : {'mrange': 100e-3, 'reading': 0.35, 'range': 0.04},
                      20e3 : {'mrange': 100e-3, 'reading': 0.06, 'range': 0.04},
                      50e3 : {'mrange': 100e-3, 'reading': 0.12, 'range': 0.05},
                      100e3: {'mrange': 100e-3, 'reading': 0.60, 'range': 0.08},
                      300e3: {'mrange': 100e-3, 'reading': 4.00, 'range': 0.50},
                      1e6  : {'mrange': 100e-3, 'reading': 30.0, 'range': 0.50}
                    },
            1     : { 5    : {'mrange': 1, 'reading': 1.00, 'range': 0.03},
                      10   : {'mrange': 1, 'reading': 0.35, 'range': 0.03},
                      20e3 : {'mrange': 1, 'reading': 0.06, 'range': 0.03},
                      50e3 : {'mrange': 1, 'reading': 0.12, 'range': 0.04},
                      100e3: {'mrange': 1, 'reading': 0.60, 'range': 0.08},
                      300e3: {'mrange': 1, 'reading': 4.00, 'range': 0.50},
                      1e6  : {'mrange': 1, 'reading': 30.0, 'range': 0.50}
                    },
            10    : { 5    : {'mrange': 10, 'reading': 1.00, 'range': 0.03},
                      10   : {'mrange': 10, 'reading': 0.35, 'range': 0.03},
                      20e3 : {'mrange': 10, 'reading': 0.06, 'range': 0.03},
                      50e3 : {'mrange': 10, 'reading': 0.12, 'range': 0.04},
                      100e3: {'mrange': 10, 'reading': 0.60, 'range': 0.08},
                      300e3: {'mrange': 10, 'reading': 4.00, 'range': 0.50},
                      1e6  : {'mrange': 10, 'reading': 30.0, 'range': 0.50}
                    },
            100   : { 5    : {'mrange': 100, 'reading': 1.00, 'range': 0.03},
                      10   : {'mrange': 100, 'reading': 0.35, 'range': 0.03},
                      20e3 : {'mrange': 100, 'reading': 0.06, 'range': 0.03},
                      50e3 : {'mrange': 100, 'reading': 0.12, 'range': 0.04},
                      100e3: {'mrange': 100, 'reading': 0.60, 'range': 0.08},
                      300e3: {'mrange': 100, 'reading': 4.00, 'range': 0.50},
                      1e6  : {'mrange': 100, 'reading': 30.0, 'range': 0.50}
                    },
            750   : { 5    : {'mrange': 1000, 'reading': 1.00, 'range': 0.03},
                      10   : {'mrange': 1000, 'reading': 0.35, 'range': 0.03},
                      20e3 : {'mrange': 1000, 'reading': 0.06, 'range': 0.03},
                      50e3 : {'mrange': 1000, 'reading': 0.12, 'range': 0.04},
                      100e3: {'mrange': 1000, 'reading': 0.60, 'range': 0.08},
                      300e3: {'mrange': 1000, 'reading': 4.00, 'range': 0.50},
                      1e6  : {'mrange': 1000, 'reading': 30.0, 'range': 0.50}
                    }
        },

        'OHM2W': {
            100   : {'mrange': 100  , 'reading': 0.010, 'range': 0.004},
            1e3   : {'mrange': 1e3  , 'reading': 0.010, 'range': 0.001},
            10e3  : {'mrange': 10e3 , 'reading': 0.010, 'range': 0.001},
            100e3 : {'mrange': 100e3, 'reading': 0.010, 'range': 0.001},
            1e6   : {'mrange': 1e6  , 'reading': 0.010, 'range': 0.001},
            10e6  : {'mrange': 10e6 , 'reading': 0.040, 'range': 0.001},
            100e6 : {'mrange': 100e6, 'reading': 0.800, 'range': 0.001}
        },

        'OHM4W': {
            100   : {'mrange': 100  ,'reading': 0.010, 'range': 0.004},
            1e3   : {'mrange': 1e3  ,'reading': 0.010, 'range': 0.001},
            10e3  : {'mrange': 10e3 ,'reading': 0.010, 'range': 0.001},
            100e3 : {'mrange': 100e3,'reading': 0.010, 'range': 0.001},
            1e6   : {'mrange': 1e6  ,'reading': 0.010, 'range': 0.001},
            10e6  : {'mrange': 10e6 ,'reading': 0.040, 'range': 0.001},
            100e6 : {'mrange': 100e6,'reading': 0.800, 'range': 0.001}
        },
        
        'DCI': {
            10e-3  : {'mrange': 10e-3 , 'reading': 0.050, 'range': 0.020},
            100e-3 : {'mrange': 100e-3, 'reading': 0.050, 'range': 0.005},
            1      : {'mrange': 1     , 'reading': 0.100, 'range': 0.010},
            3      : {'mrange': 3     , 'reading': 0.120, 'range': 0.020}
        },
        
        'ACI': {
            1 : { 5   : {'mrange': 1, 'reading': 0.0050, 'range': 0.0035},
                  10  : {'mrange': 1, 'reading': 0.0050, 'range': 0.0035},
                  5e3 : {'mrange': 1, 'reading': 0.0050, 'range': 0.0035}
                },
            3 : {
                  5   : {'mrange': 3, 'reading': 0.0050, 'range': 0.0035},
                  10  : {'mrange': 3, 'reading': 0.0050, 'range': 0.0035},
                  5e3 : {'mrange': 3, 'reading': 0.0050, 'range': 0.0035}
                }
        }
        
        
    }  
    
    spec = { '1 year': spec_1year }
    
    
    def init(self):
        self.set_timeout(10)
        self.idstr  = self.query("*IDN?").strip()
        self.calstr = self.query("CALibration:STRing?").strip().replace('"', "")
        

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
    

    def trigger_read(self):
        self.write("INIT")


    def get_triggered_read(self):
        return float(self.query("FETCH?"))


    def __conf_range(self, prefix:str, range):
        #self.write("CONF:{0:s}".format(prefix))
        
        if range is None:
            #self.write("{0:s}:RANGE:AUTO ON".format(prefix))
            self.write("CONF:{0:s}".format(prefix))
        else:
            self.write("CONF:{0:s} {1:0.6f}".format(prefix, range))
            #self.write("{0:s}:RANGE {1:0.6f}".format(prefix, range)
            
        
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
        self.mode = 'DCV'
        self.mrange = mrange


    def conf_function_DCI(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCI. if range=None the meter is set to Autorange"""
        self.__conf_range("CURR:DC", mrange)
        self.write("CURR:DC:NPLC {0:0.3f}".format(nplc))
        self.__autoZero(AutoZero)
        self.mode = 'DCI'
        self.mrange = mrange


    def conf_function_ACV(self, mrange=None, nplc=None, AutoZero=True, HiZ=True, filter=3, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__conf_range("VOLT:AC", mrange)
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)

        #AC Filter Bandwitch can be 3Hz, 20Hz, 200Hz
        self.write("SENSe:DETector:BANDwidth {0:d}".format(filter))
        self.mode = 'ACV'
        self.mrange = mrange


    def conf_function_ACI(self, mrange=None, nplc=None, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__conf_range("CURR:AC", mrange)
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)
        self.mode = 'ACI'
        self.mrange = mrange


    def conf_function_OHM2W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__conf_range("RES", mrange)
        self.write("RES:NPLC {0:0.3f}".format(nplc))
        self.mode = 'OHM2W'
        self.mrange = mrange
        

    def conf_function_OHM4W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__conf_range("FRES", mrange)
        self.write("FRES:NPLC {0:0.3f}".format(nplc))
        self.mode = 'OHM4W'
        self.mrange = mrange
        
    
    def conf_function_FREQ(self, mrange=None, nplc=None, AutoZero=True, HiZ=True, filter=3, channel=1):
        """configures the meter to measure Frequency. if range=None the meter is set to Autorange"""
        self.write("CONF:FREQ")
        self.write("FREQ:APER 0.1")
        
        
    def set_mode(self, mode, mrange=None):
        if mode == "DCV":
            self.conf_function_DCV(mrange=mrange)
            return
        
        if mode == "ACV":
            self.conf_function_ACV(mrange=mrange)
            return
        
        if mode == "DCI":
            self.conf_function_DCI(mrange=mrange)
            return

        if mode == "ACI":
            self.conf_function_ACI(mrange=mrange)
            return
        
        if mode == "OHM2W":
            self.conf_function_OHM2W(mrange=mrange)
            return

        if mode == "OHM4W":
            self.conf_function_OHM4W(mrange=mrange)
            return
        
        if mode == "FREQ":
            self.conf_function_FREQ(mrange=mrange)
            return
        
        print("Mode not supported!")

        
        