# Keysight 34461A 6.5 digit DMM

import testgear.base_classes as base
import testgear.HPAK as HPAK

class K34461A(HPAK.HP34401A):
    spec_1year = { 
        'DCV': { 
            120e-3: {'mrange': 100e-3, 'reading': 0.0050, 'range': 0.0035},
            1.2   : {'mrange': 1     , 'reading': 0.0040, 'range': 0.0007},
            12    : {'mrange': 10    , 'reading': 0.0035, 'range': 0.0005},
            120   : {'mrange': 100   , 'reading': 0.0045, 'range': 0.0006},
            1000  : {'mrange': 1000  , 'reading': 0.0045, 'range': 0.0010}
        },
        
        'ACV': {
            100e-3: { 5    : {'mrange': 100e-3, 'reading': 1.00, 'range': 0.03},
                      10   : {'mrange': 100e-3, 'reading': 0.35, 'range': 0.03},
                      20e3 : {'mrange': 100e-3, 'reading': 0.06, 'range': 0.03},
                      50e3 : {'mrange': 100e-3, 'reading': 0.12, 'range': 0.05},
                      100e3: {'mrange': 100e-3, 'reading': 0.60, 'range': 0.08},
                      300e3: {'mrange': 100e-3, 'reading': 4.00, 'range': 0.50}
                    },
            1     : { 5    : {'mrange': 1, 'reading': 1.00, 'range': 0.03},
                      10   : {'mrange': 1, 'reading': 0.35, 'range': 0.03},
                      20e3 : {'mrange': 1, 'reading': 0.06, 'range': 0.03},
                      50e3 : {'mrange': 1, 'reading': 0.12, 'range': 0.05},
                      100e3: {'mrange': 1, 'reading': 0.60, 'range': 0.08},
                      300e3: {'mrange': 1, 'reading': 4.00, 'range': 0.50}
                    },
            10    : { 5    : {'mrange': 10, 'reading': 1.00, 'range': 0.03},
                      10   : {'mrange': 10, 'reading': 0.35, 'range': 0.03},
                      20e3 : {'mrange': 10, 'reading': 0.06, 'range': 0.03},
                      50e3 : {'mrange': 10, 'reading': 0.12, 'range': 0.05},
                      100e3: {'mrange': 10, 'reading': 0.60, 'range': 0.08},
                      300e3: {'mrange': 10, 'reading': 4.00, 'range': 0.50}
                    },
            100   : { 5    : {'mrange': 100, 'reading': 1.00, 'range': 0.03},
                      10   : {'mrange': 100, 'reading': 0.35, 'range': 0.03},
                      20e3 : {'mrange': 100, 'reading': 0.06, 'range': 0.03},
                      50e3 : {'mrange': 100, 'reading': 0.12, 'range': 0.05},
                      100e3: {'mrange': 100, 'reading': 0.60, 'range': 0.08},
                      300e3: {'mrange': 100, 'reading': 4.00, 'range': 0.50}
                    },
            750   : { 5    : {'mrange': 750, 'reading': 1.00, 'range': 0.03},
                      10   : {'mrange': 750, 'reading': 0.35, 'range': 0.03},
                      20e3 : {'mrange': 750, 'reading': 0.06, 'range': 0.03},
                      50e3 : {'mrange': 750, 'reading': 0.12, 'range': 0.05},
                      100e3: {'mrange': 750, 'reading': 0.60, 'range': 0.08},
                      300e3: {'mrange': 750, 'reading': 4.00, 'range': 0.50}
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
            100   : {'mrange': 100  , 'reading': 0.010, 'range': 0.004},
            1e3   : {'mrange': 1e3  , 'reading': 0.010, 'range': 0.001},
            10e3  : {'mrange': 10e3 , 'reading': 0.010, 'range': 0.001},
            100e3 : {'mrange': 100e3, 'reading': 0.010, 'range': 0.001},
            1e6   : {'mrange': 1e6  , 'reading': 0.010, 'range': 0.001},
            10e6  : {'mrange': 10e6 , 'reading': 0.040, 'range': 0.001},
            100e6 : {'mrange': 100e6, 'reading': 0.800, 'range': 0.001}
        },
        
        'DCI': {
            100e-6 : {'mrange': 100e-6, 'reading': 0.0500, 'range': 0.0250},
            1e-3   : {'mrange': 1e-3  , 'reading': 0.0500, 'range': 0.0060},
            10e-3  : {'mrange': 10e-3 , 'reading': 0.0500, 'range': 0.0200},
            100e-3 : {'mrange': 100e-3, 'reading': 0.0500, 'range': 0.0050},
            1      : {'mrange': 1     , 'reading': 0.1000, 'range': 0.0100},
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
            10    : {'mrange': 10   , 'reading': 0.100, 'range': 0},
            100   : {'mrange': 100  , 'reading': 0.030, 'range': 0},
            1e3   : {'mrange': 1e3  , 'reading': 0.010, 'range': 0},
            300e3 : {'mrange': 300e3, 'reading': 0.010, 'range': 0}
        }
        
    }  
    
    spec = { '1 year': spec_1year }
