# Keysight 34470A 7.5 digit DMM

import testgear.base_classes as base
import testgear.HPAK as HPAK
import numpy as np
class K34470A(HPAK.K34461A):

    def digitize_conf(self, mrange=10, samples=30000, srate=0, aperture=0, delay=0):
        self.write("*RST")
        self.write('CONF:VOLT:DC 10')
        self.write('SENS:VOLT:DC:NPLC 0.001')
        self.write('SENS:VOLT:DC:ZERO:AUTO 0')
        self.write('SENS:VOLT:DC:IMPEDANCE:AUTO ON')
        self.write('TRIG:SOUR INT')
        self.write('TRIG:SLOP POS')
        self.write('TRIG:DEL 0')
        self.write('TRIG:LEV 0')
        self.write('SAMP:SOUR TIM')
        self.write('SAMP:TIM MIN')
        self.write('SAMP:COUN '+str(samples))
        self.write('SAMP:COUN:PRET 250')


    def digitize_arm(self):
        self.write("INIT")


    def digitize_read(self):
        values    = list(map(float, self.query("FETCH?").split(",")))
        value_cnt = len(values)
        dt        = float(self.query('SAMP:TIM?'))
        t         = np.linspace(0, value_cnt * dt, value_cnt)
        return t, np.array(values)


    spec_1year = { 
        'DCV': { 
            120e-3: {'mrange': 100e-3, 'reading': 0.0040, 'range': 0.0035},
            1.2   : {'mrange': 1     , 'reading': 0.0020, 'range': 0.0004},
            12    : {'mrange': 10    , 'reading': 0.0016, 'range': 0.0002},
            120   : {'mrange': 100   , 'reading': 0.0038, 'range': 0.0006},
            1000  : {'mrange': 1000  , 'reading': 0.0038, 'range': 0.0006}
        },
        
        'ACV': {
            100e-3: { 5    : {'mrange': 100e-3, 'reading': 0.50, 'range': 0.02},
                      10   : {'mrange': 100e-3, 'reading': 0.10, 'range': 0.02},
                      20e3 : {'mrange': 100e-3, 'reading': 0.05, 'range': 0.02},
                      50e3 : {'mrange': 100e-3, 'reading': 0.07, 'range': 0.03},
                      100e3: {'mrange': 100e-3, 'reading': 0.15, 'range': 0.05},
                      300e3: {'mrange': 100e-3, 'reading': 1.00, 'range': 0.10}
                    },
            1     : { 5    : {'mrange': 100e-3, 'reading': 0.50, 'range': 0.02},
                      10   : {'mrange': 100e-3, 'reading': 0.10, 'range': 0.02},
                      20e3 : {'mrange': 100e-3, 'reading': 0.05, 'range': 0.02},
                      50e3 : {'mrange': 100e-3, 'reading': 0.07, 'range': 0.03},
                      100e3: {'mrange': 100e-3, 'reading': 0.15, 'range': 0.05},
                      300e3: {'mrange': 100e-3, 'reading': 1.00, 'range': 0.10}
                    },
            10    : { 5    : {'mrange': 100e-3, 'reading': 0.50, 'range': 0.02},
                      10   : {'mrange': 100e-3, 'reading': 0.10, 'range': 0.02},
                      20e3 : {'mrange': 100e-3, 'reading': 0.05, 'range': 0.02},
                      50e3 : {'mrange': 100e-3, 'reading': 0.07, 'range': 0.03},
                      100e3: {'mrange': 100e-3, 'reading': 0.15, 'range': 0.05},
                      300e3: {'mrange': 100e-3, 'reading': 1.00, 'range': 0.10}
                    },
            100   : { 5    : {'mrange': 100e-3, 'reading': 0.50, 'range': 0.02},
                      10   : {'mrange': 100e-3, 'reading': 0.10, 'range': 0.02},
                      20e3 : {'mrange': 100e-3, 'reading': 0.05, 'range': 0.02},
                      50e3 : {'mrange': 100e-3, 'reading': 0.07, 'range': 0.03},
                      100e3: {'mrange': 100e-3, 'reading': 0.15, 'range': 0.05},
                      300e3: {'mrange': 100e-3, 'reading': 1.00, 'range': 0.10}
                    },
            750   : { 5    : {'mrange': 100e-3, 'reading': 0.50, 'range': 0.02},
                      10   : {'mrange': 100e-3, 'reading': 0.10, 'range': 0.02},
                      20e3 : {'mrange': 100e-3, 'reading': 0.05, 'range': 0.02},
                      50e3 : {'mrange': 100e-3, 'reading': 0.07, 'range': 0.03},
                      100e3: {'mrange': 100e-3, 'reading': 0.15, 'range': 0.05},
                      300e3: {'mrange': 100e-3, 'reading': 1.00, 'range': 0.10}
                    }
        },

        'OHM2W': {
            100   : {'mrange': 100  , 'reading': 0.0060, 'range': 0.0040},
            1e3   : {'mrange': 1e3  , 'reading': 0.0040, 'range': 0.0005},
            10e3  : {'mrange': 10e3 , 'reading': 0.0040, 'range': 0.0005},
            100e3 : {'mrange': 100e3, 'reading': 0.0040, 'range': 0.0005},
            1e6   : {'mrange': 1e6  , 'reading': 0.0070, 'range': 0.0005},
            10e6  : {'mrange': 10e6 , 'reading': 0.0250, 'range': 0.0010},
            100e6 : {'mrange': 100e6, 'reading': 0.3000, 'range': 0.0010},
            1e9   : {'mrange': 1e9  , 'reading': 3.0000, 'range': 0.0010}
        },

        'OHM4W': {
            100   : {'mrange': 100  , 'reading': 0.0060, 'range': 0.0040},
            1e3   : {'mrange': 1e3  , 'reading': 0.0040, 'range': 0.0005},
            10e3  : {'mrange': 10e3 , 'reading': 0.0040, 'range': 0.0005},
            100e3 : {'mrange': 100e3, 'reading': 0.0040, 'range': 0.0005},
            1e6   : {'mrange': 1e6  , 'reading': 0.0070, 'range': 0.0005},
            10e6  : {'mrange': 10e6 , 'reading': 0.0250, 'range': 0.0010},
            100e6 : {'mrange': 100e6, 'reading': 0.3000, 'range': 0.0010},
            1e9   : {'mrange': 1e9  , 'reading': 3.0000, 'range': 0.0010}
        },
        
        'DCI': {
            1-6    : {'mrange': 100e-6, 'reading': 0.0500, 'range': 0.0050},
            10e-6  : {'mrange': 100e-6, 'reading': 0.0500, 'range': 0.0020},
            100e-6 : {'mrange': 100e-6, 'reading': 0.0500, 'range': 0.0010},
            1e-3   : {'mrange': 1e-3  , 'reading': 0.0500, 'range': 0.0050},
            10e-3  : {'mrange': 10e-3 , 'reading': 0.0500, 'range': 0.0200},
            100e-3 : {'mrange': 100e-3, 'reading': 0.0500, 'range': 0.0050},
            1      : {'mrange': 1     , 'reading': 0.0800, 'range': 0.0100},
            3      : {'mrange': 3     , 'reading': 0.2000, 'range': 0.0200},
            10     : {'mrange': 10    , 'reading': 0.1200, 'range': 0.0100}
        },
        
        'ACI': {
            100e-6: { 10e3 : {'mrange': 100e-6, 'reading': 0.10, 'range': 0.04} },
            1e-3  : { 10e3 : {'mrange': 1e-3  , 'reading': 0.10, 'range': 0.04} },
            10e-3 : { 10e3 : {'mrange': 10e-3 , 'reading': 0.10, 'range': 0.04} },
            100e-3: { 10e3 : {'mrange': 100e-3, 'reading': 0.10, 'range': 0.04} },
            1     : { 10e3 : {'mrange': 1     , 'reading': 0.10, 'range': 0.04} },
            3     : { 10e3 : {'mrange': 3     , 'reading': 0.23, 'range': 0.04} },
            10    : { 10e3 : {'mrange': 10    , 'reading': 0.15, 'range': 0.04} }
        },
        
        'FREQ': {
            10    : {'mrange': 10   , 'reading': 0.070, 'range': 0},
            100   : {'mrange': 100  , 'reading': 0.030, 'range': 0},
            1e3   : {'mrange': 1e3  , 'reading': 0.007, 'range': 0},
            300e3 : {'mrange': 300e3, 'reading': 0.006, 'range': 0}
        }
        
    }  
    
    spec = { '1 year': spec_1year }

    
    
    cal1 = [
        {'mode': 'DCI', 'mrange': 10     , 'value': 2     , 'frequency': 0},
        ]
    
    cal2 = [
        {'mode': 'DCV', 'mrange': 100e-3, 'value': 100e-3, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 1     , 'value': 1     , 'frequency': 0},
        {'mode': 'DCV', 'mrange': 10    , 'value': 10    , 'frequency': 0},
        {'mode': 'DCV', 'mrange': 10    , 'value': -10   , 'frequency': 0},
        {'mode': 'DCV', 'mrange': 100   , 'value': 100   , 'frequency': 0},
        {'mode': 'DCV', 'mrange': 1000  , 'value': 1000  , 'frequency': 0},

        {'mode': 'ACV', 'mrange': 100e-3, 'value': 100e-3, 'frequency': 1e3  },
        {'mode': 'ACV', 'mrange': 100e-3, 'value': 100e-3, 'frequency': 50e3 },
        {'mode': 'ACV', 'mrange': 1     , 'value': 1     , 'frequency': 1e3  },
        {'mode': 'ACV', 'mrange': 1     , 'value': 1     , 'frequency': 50e3 },
        {'mode': 'ACV', 'mrange': 10    , 'value': 10    , 'frequency': 10   },
        {'mode': 'ACV', 'mrange': 10    , 'value': 10    , 'frequency': 1e3  },
        {'mode': 'ACV', 'mrange': 10    , 'value': 10    , 'frequency': 20e3 },
        {'mode': 'ACV', 'mrange': 10    , 'value': 10    , 'frequency': 50e3 },
        {'mode': 'ACV', 'mrange': 10    , 'value': 10    , 'frequency': 100e3},
        {'mode': 'ACV', 'mrange': 10    , 'value': 10    , 'frequency': 300e3},
        {'mode': 'ACV', 'mrange': 100   , 'value': 100   , 'frequency': 1e3  },
        {'mode': 'ACV', 'mrange': 100   , 'value': 100   , 'frequency': 50e3 },
        {'mode': 'ACV', 'mrange': 750   , 'value': 750   , 'frequency': 1e3  },

        {'mode': 'OHM4W', 'mrange': 100  , 'value': 100  , 'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 1e3  , 'value': 1e3  , 'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 10e3 , 'value': 10e3 , 'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 100e3, 'value': 100e3, 'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 1e6  , 'value': 1e6  , 'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 10e6 , 'value': 10e6 , 'frequency': 0},

        {'mode': 'DCI', 'mrange': 10e-3 , 'value': 10e-3 , 'frequency': 0},
        {'mode': 'DCI', 'mrange': 100e-3, 'value': 100e-3, 'frequency': 0},
        {'mode': 'DCI', 'mrange': 1     , 'value': 1     , 'frequency': 0},
        {'mode': 'DCI', 'mrange': 3     , 'value': 2     , 'frequency': 0},

        {'mode': 'ACI', 'mrange': 10e-3 , 'value': 10e-3 , 'frequency': 1e3},
        {'mode': 'ACI', 'mrange': 100e-3, 'value': 100e-3, 'frequency': 1e3},
        {'mode': 'ACI', 'mrange': 1     , 'value': 1     , 'frequency': 1e3},
        {'mode': 'ACI', 'mrange': 3     , 'value': 2     , 'frequency': 1e3},

        {'mode': 'FREQ', 'mrange': 100e-3, 'value': 100e-3 , 'frequency': 300e3}

        ]
    
    
    callist = [
        {'instruction': "Connect the Fluke 5730A to the 10A input", 'calpoints': cal1},
        {'instruction': "Connect the Fluke 5730A to Input, Sense and the 3A input", 'calpoints': cal2}     
    ]