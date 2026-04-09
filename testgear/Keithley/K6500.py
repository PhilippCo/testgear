import testgear.base_classes as base

class K6500(base.meter):
    """
    Keithley DMM6500 6.5 digit DMM
    Native SCPI implementation.

    Notes:
    - Specs below are based on the published DMM6500 datasheet 1-year values.
    - Calibration / verification points are based on the DMM6500 calibration manual.
    - Frequency is included in cal points, but not as a clean 1-year spec table here,
      because the public datasheet publishes the generic frequency table as 2-year.
    """

    spec_1year = {
        'DCV': {
            120e-3: {'mrange': 100e-3, 'reading': 0.0030, 'range': 0.0035},
            1.2:    {'mrange': 1,      'reading': 0.0025, 'range': 0.0006},
            12:     {'mrange': 10,     'reading': 0.0025, 'range': 0.0005},
            120:    {'mrange': 100,    'reading': 0.0040, 'range': 0.0006},
            1000:   {'mrange': 1000,   'reading': 0.0040, 'range': 0.0006},
        },

        # ACV spec by frequency band from datasheet 1-year values
        # Bands:
        # 3-5 Hz, 5-10 Hz, 10 Hz-20 kHz, 20-50 kHz, 50-100 kHz, 100-300 kHz
        'ACV': {
            100e-3: {
                4:      {'mrange': 100e-3, 'reading': 1.00, 'range': 0.03},
                7:      {'mrange': 100e-3, 'reading': 0.35, 'range': 0.03},
                1e3:    {'mrange': 100e-3, 'reading': 0.06, 'range': 0.03},
                50e3:   {'mrange': 100e-3, 'reading': 0.12, 'range': 0.05},
                100e3:  {'mrange': 100e-3, 'reading': 0.60, 'range': 0.08},
                300e3:  {'mrange': 100e-3, 'reading': 4.00, 'range': 0.50},
            },
            1: {
                4:      {'mrange': 1, 'reading': 1.00, 'range': 0.03},
                7:      {'mrange': 1, 'reading': 0.35, 'range': 0.03},
                1e3:    {'mrange': 1, 'reading': 0.06, 'range': 0.03},
                50e3:   {'mrange': 1, 'reading': 0.12, 'range': 0.05},
                100e3:  {'mrange': 1, 'reading': 0.60, 'range': 0.08},
                300e3:  {'mrange': 1, 'reading': 4.00, 'range': 0.50},
            },
            10: {
                4:      {'mrange': 10, 'reading': 1.00, 'range': 0.03},
                7:      {'mrange': 10, 'reading': 0.35, 'range': 0.03},
                1e3:    {'mrange': 10, 'reading': 0.06, 'range': 0.03},
                50e3:   {'mrange': 10, 'reading': 0.12, 'range': 0.05},
                100e3:  {'mrange': 10, 'reading': 0.60, 'range': 0.08},
                300e3:  {'mrange': 10, 'reading': 4.00, 'range': 0.50},
            },
            100: {
                4:      {'mrange': 100, 'reading': 1.00, 'range': 0.03},
                7:      {'mrange': 100, 'reading': 0.35, 'range': 0.03},
                1e3:    {'mrange': 100, 'reading': 0.06, 'range': 0.03},
                50e3:   {'mrange': 100, 'reading': 0.12, 'range': 0.05},
                100e3:  {'mrange': 100, 'reading': 0.60, 'range': 0.08},
                300e3:  {'mrange': 100, 'reading': 4.00, 'range': 0.50},
            },
            750: {
                4:      {'mrange': 750, 'reading': 1.00, 'range': 0.03},
                7:      {'mrange': 750, 'reading': 0.35, 'range': 0.03},
                1e3:    {'mrange': 750, 'reading': 0.06, 'range': 0.03},
                50e3:   {'mrange': 750, 'reading': 0.12, 'range': 0.05},
                100e3:  {'mrange': 750, 'reading': 0.60, 'range': 0.08},
                300e3:  {'mrange': 750, 'reading': 4.00, 'range': 0.50},
            }
        },

        # For OHM2W, low-ohm lead uncertainty is not folded in here.
        # 1 ohm is 4W only, so OHM2W starts at 100 ohm here.
        'OHM2W': {
            100:    {'mrange': 100,    'reading': 0.0085, 'range': 0.0020},
            1e3:    {'mrange': 1e3,    'reading': 0.0075, 'range': 0.0006},
            10e3:   {'mrange': 10e3,   'reading': 0.0075, 'range': 0.0006},
            100e3:  {'mrange': 100e3,  'reading': 0.0075, 'range': 0.0010},
            1e6:    {'mrange': 1e6,    'reading': 0.0100, 'range': 0.0006},
            10e6:   {'mrange': 10e6,   'reading': 0.0400, 'range': 0.0010},
            100e6:  {'mrange': 100e6,  'reading': 0.2000, 'range': 0.0030},
        },

        'OHM4W': {
            1:      {'mrange': 1,      'reading': 0.0085, 'range': 0.0200},
            10:     {'mrange': 10,     'reading': 0.0085, 'range': 0.0020},
            100:    {'mrange': 100,    'reading': 0.0085, 'range': 0.0020},
            1e3:    {'mrange': 1e3,    'reading': 0.0075, 'range': 0.0006},
            10e3:   {'mrange': 10e3,   'reading': 0.0075, 'range': 0.0006},
            100e3:  {'mrange': 100e3,  'reading': 0.0075, 'range': 0.0010},
            1e6:    {'mrange': 1e6,    'reading': 0.0100, 'range': 0.0006},
            10e6:   {'mrange': 10e6,   'reading': 0.0400, 'range': 0.0010},
            100e6:  {'mrange': 100e6,  'reading': 0.2000, 'range': 0.0030},
        },

        'DCI': {
            10e-6:   {'mrange': 10e-6,   'reading': 0.045, 'range': 0.005},
            100e-6:  {'mrange': 100e-6,  'reading': 0.045, 'range': 0.005},
            1e-3:    {'mrange': 1e-3,    'reading': 0.045, 'range': 0.005},
            10e-3:   {'mrange': 10e-3,   'reading': 0.020, 'range': 0.005},
            100e-3:  {'mrange': 100e-3,  'reading': 0.020, 'range': 0.005},
            1:       {'mrange': 1,       'reading': 0.040, 'range': 0.005},
            3:       {'mrange': 3,       'reading': 0.050, 'range': 0.004},
            10:      {'mrange': 10,      'reading': 0.220, 'range': 0.025},
        },

        'ACI': {
            100e-6: {
                40:   {'mrange': 100e-6, 'reading': 0.10, 'range': 0.07},
                1e3:  {'mrange': 100e-6, 'reading': 0.10, 'range': 0.07},
                5e3:  {'mrange': 100e-6, 'reading': 0.15, 'range': 0.07},
            },
            1e-3: {
                40:   {'mrange': 1e-3, 'reading': 0.10, 'range': 0.04},
                1e3:  {'mrange': 1e-3, 'reading': 0.10, 'range': 0.04},
                5e3:  {'mrange': 1e-3, 'reading': 0.10, 'range': 0.04},
            },
            10e-3: {
                40:   {'mrange': 10e-3, 'reading': 0.10, 'range': 0.04},
                1e3:  {'mrange': 10e-3, 'reading': 0.10, 'range': 0.04},
                5e3:  {'mrange': 10e-3, 'reading': 0.10, 'range': 0.04},
            },
            100e-3: {
                40:   {'mrange': 100e-3, 'reading': 0.10, 'range': 0.04},
                1e3:  {'mrange': 100e-3, 'reading': 0.10, 'range': 0.04},
                5e3:  {'mrange': 100e-3, 'reading': 0.10, 'range': 0.04},
            },
            1: {
                40:   {'mrange': 1, 'reading': 0.10, 'range': 0.04},
                1e3:  {'mrange': 1, 'reading': 0.10, 'range': 0.04},
                5e3:  {'mrange': 1, 'reading': 0.15, 'range': 0.06},
            },
            3: {
                40:   {'mrange': 3, 'reading': 0.15, 'range': 0.06},
                1e3:  {'mrange': 3, 'reading': 0.15, 'range': 0.06},
                5e3:  {'mrange': 3, 'reading': 0.15, 'range': 0.06},
            },
            10: {
                40:   {'mrange': 10, 'reading': 0.40, 'range': 0.06},
                1e3:  {'mrange': 10, 'reading': 0.40, 'range': 0.06},
                5e3:  {'mrange': 10, 'reading': 1.00, 'range': 0.07},
            },
        },


        'FREQ': {
            10    : {'mrange': 10   , 'reading': 0.050, 'range': 0},
            100   : {'mrange': 100  , 'reading': 0.010, 'range': 0},
            1e3   : {'mrange': 1e3  , 'reading': 0.005, 'range': 0},
            300e3 : {'mrange': 300e3, 'reading': 0.005, 'range': 0}
        }
    }

    spec = {'1 year': spec_1year}

    # Optional zero-check list
    cal1 = [
        {'mode': 'DCV', 'mrange': 100e-3, 'value': 0, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 1,      'value': 0, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 10,     'value': 0, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 100,    'value': 0, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 1000,   'value': 0, 'frequency': 0},

        {'mode': 'OHM4W', 'mrange': 1,    'value': 0, 'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 10,   'value': 0, 'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 100,  'value': 0, 'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 1e3,  'value': 0, 'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 10e3, 'value': 0, 'frequency': 0},

        {'mode': 'OHM2W', 'mrange': 100e3, 'value': 0, 'frequency': 0},
        {'mode': 'OHM2W', 'mrange': 1e6,   'value': 0, 'frequency': 0},
        {'mode': 'OHM2W', 'mrange': 10e6,  'value': 0, 'frequency': 0},
        {'mode': 'OHM2W', 'mrange': 100e6, 'value': 0, 'frequency': 0},
    ]

    # Keithley/Tek recommended verification points
    cal2 = [
        # DCV: full-scale and half-scale, plus polarity reversal
        {'mode': 'DCV', 'mrange': 100e-3, 'value': 100e-3, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 100e-3, 'value': 50e-3,  'frequency': 0},
        {'mode': 'DCV', 'mrange': 100e-3, 'value': -50e-3, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 100e-3, 'value': -100e-3, 'frequency': 0},

        {'mode': 'DCV', 'mrange': 1, 'value': 1, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 1, 'value': 0.5, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 1, 'value': -0.5, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 1, 'value': -1, 'frequency': 0},

        {'mode': 'DCV', 'mrange': 10, 'value': 10, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 10, 'value': 5, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 10, 'value': -5, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 10, 'value': -10, 'frequency': 0},

        {'mode': 'DCV', 'mrange': 100, 'value': 100, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 100, 'value': 50, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 100, 'value': -50, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 100, 'value': -100, 'frequency': 0},

        {'mode': 'DCV', 'mrange': 1000, 'value': 1000, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 1000, 'value': 500, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 1000, 'value': -500, 'frequency': 0},
        {'mode': 'DCV', 'mrange': 1000, 'value': -1000, 'frequency': 0},

        # ACV recommended verification points
        {'mode': 'ACV', 'mrange': 100e-3, 'value': 100e-3, 'frequency': 30},
        {'mode': 'ACV', 'mrange': 100e-3, 'value': 100e-3, 'frequency': 1e3},
        {'mode': 'ACV', 'mrange': 100e-3, 'value': 100e-3, 'frequency': 50e3},
        {'mode': 'ACV', 'mrange': 100e-3, 'value': 100e-3, 'frequency': 100e3},

        {'mode': 'ACV', 'mrange': 1, 'value': 1, 'frequency': 30},
        {'mode': 'ACV', 'mrange': 1, 'value': 1, 'frequency': 1e3},
        {'mode': 'ACV', 'mrange': 1, 'value': 1, 'frequency': 50e3},
        {'mode': 'ACV', 'mrange': 1, 'value': 1, 'frequency': 100e3},

        {'mode': 'ACV', 'mrange': 10, 'value': 10, 'frequency': 30},
        {'mode': 'ACV', 'mrange': 10, 'value': 10, 'frequency': 1e3},
        {'mode': 'ACV', 'mrange': 10, 'value': 10, 'frequency': 50e3},
        {'mode': 'ACV', 'mrange': 10, 'value': 10, 'frequency': 100e3},

        {'mode': 'ACV', 'mrange': 100, 'value': 100, 'frequency': 30},
        {'mode': 'ACV', 'mrange': 100, 'value': 100, 'frequency': 1e3},
        {'mode': 'ACV', 'mrange': 100, 'value': 100, 'frequency': 50e3},
        {'mode': 'ACV', 'mrange': 100, 'value': 100, 'frequency': 100e3},

        {'mode': 'ACV', 'mrange': 750, 'value': 740, 'frequency': 50},
        {'mode': 'ACV', 'mrange': 750, 'value': 740, 'frequency': 1e3},
        {'mode': 'ACV', 'mrange': 750, 'value': 740, 'frequency': 50e3},
        {'mode': 'ACV', 'mrange': 750, 'value': 740, 'frequency': 100e3},

        # 4W resistance verification points
        {'mode': 'OHM4W', 'mrange': 1,     'value': 0,     'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 1,     'value': 1,     'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 10,    'value': 0,     'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 10,    'value': 10,    'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 100,   'value': 0,     'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 100,   'value': 100,   'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 1e3,   'value': 0,     'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 1e3,   'value': 1e3,   'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 10e3,  'value': 0,     'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 10e3,  'value': 10e3,  'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 100e3, 'value': 0,     'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 100e3, 'value': 100e3, 'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 1e6,   'value': 0,     'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 1e6,   'value': 1e6,   'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 10e6,  'value': 0,     'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 10e6,  'value': 10e6,  'frequency': 0},

        # 2W resistance recommended point from manual
        {'mode': 'OHM2W', 'mrange': 100e6, 'value': 0,      'frequency': 0},
        {'mode': 'OHM2W', 'mrange': 100e6, 'value': 100e6,  'frequency': 0},

        # DCI verification points
        {'mode': 'DCI', 'mrange': 10e-6,  'value': 10e-6,  'frequency': 0},
        {'mode': 'DCI', 'mrange': 10e-6,  'value': 5e-6,   'frequency': 0},
        {'mode': 'DCI', 'mrange': 10e-6,  'value': -5e-6,  'frequency': 0},
        {'mode': 'DCI', 'mrange': 10e-6,  'value': -10e-6, 'frequency': 0},

        {'mode': 'DCI', 'mrange': 100e-6, 'value': 100e-6,  'frequency': 0},
        {'mode': 'DCI', 'mrange': 100e-6, 'value': 50e-6,   'frequency': 0},
        {'mode': 'DCI', 'mrange': 100e-6, 'value': -50e-6,  'frequency': 0},
        {'mode': 'DCI', 'mrange': 100e-6, 'value': -100e-6, 'frequency': 0},

        {'mode': 'DCI', 'mrange': 1e-3, 'value': 1e-3, 'frequency': 0},
        {'mode': 'DCI', 'mrange': 1e-3, 'value': 0.5e-3, 'frequency': 0},
        {'mode': 'DCI', 'mrange': 1e-3, 'value': -0.5e-3, 'frequency': 0},
        {'mode': 'DCI', 'mrange': 1e-3, 'value': -1e-3, 'frequency': 0},

        {'mode': 'DCI', 'mrange': 10e-3, 'value': 10e-3, 'frequency': 0},
        {'mode': 'DCI', 'mrange': 10e-3, 'value': 5e-3, 'frequency': 0},
        {'mode': 'DCI', 'mrange': 10e-3, 'value': -5e-3, 'frequency': 0},
        {'mode': 'DCI', 'mrange': 10e-3, 'value': -10e-3, 'frequency': 0},

        {'mode': 'DCI', 'mrange': 100e-3, 'value': 100e-3, 'frequency': 0},
        {'mode': 'DCI', 'mrange': 100e-3, 'value': 50e-3,  'frequency': 0},
        {'mode': 'DCI', 'mrange': 100e-3, 'value': -50e-3, 'frequency': 0},
        {'mode': 'DCI', 'mrange': 100e-3, 'value': -100e-3, 'frequency': 0},

        {'mode': 'DCI', 'mrange': 1, 'value': 1, 'frequency': 0},
        {'mode': 'DCI', 'mrange': 1, 'value': 0.5, 'frequency': 0},
        {'mode': 'DCI', 'mrange': 1, 'value': -0.5, 'frequency': 0},
        {'mode': 'DCI', 'mrange': 1, 'value': -1, 'frequency': 0},

        {'mode': 'DCI', 'mrange': 3, 'value': 2, 'frequency': 0},
        {'mode': 'DCI', 'mrange': 3, 'value': 1.5, 'frequency': 0},
        {'mode': 'DCI', 'mrange': 3, 'value': -1.5, 'frequency': 0},
        {'mode': 'DCI', 'mrange': 3, 'value': -2, 'frequency': 0},

        # ACI verification points
        {'mode': 'ACI', 'mrange': 100e-6, 'value': 100e-6, 'frequency': 40},
        {'mode': 'ACI', 'mrange': 100e-6, 'value': 100e-6, 'frequency': 1e3},

        {'mode': 'ACI', 'mrange': 1e-3, 'value': 1e-3, 'frequency': 40},
        {'mode': 'ACI', 'mrange': 1e-3, 'value': 1e-3, 'frequency': 1e3},
        {'mode': 'ACI', 'mrange': 1e-3, 'value': 1e-3, 'frequency': 5e3},

        {'mode': 'ACI', 'mrange': 10e-3, 'value': 10e-3, 'frequency': 40},
        {'mode': 'ACI', 'mrange': 10e-3, 'value': 10e-3, 'frequency': 1e3},
        {'mode': 'ACI', 'mrange': 10e-3, 'value': 10e-3, 'frequency': 5e3},

        {'mode': 'ACI', 'mrange': 100e-3, 'value': 100e-3, 'frequency': 40},
        {'mode': 'ACI', 'mrange': 100e-3, 'value': 100e-3, 'frequency': 1e3},
        {'mode': 'ACI', 'mrange': 100e-3, 'value': 100e-3, 'frequency': 5e3},

        {'mode': 'ACI', 'mrange': 1, 'value': 1, 'frequency': 40},
        {'mode': 'ACI', 'mrange': 1, 'value': 1, 'frequency': 1e3},
        {'mode': 'ACI', 'mrange': 1, 'value': 1, 'frequency': 5e3},

        {'mode': 'ACI', 'mrange': 3, 'value': 2, 'frequency': 40},
        {'mode': 'ACI', 'mrange': 3, 'value': 2, 'frequency': 1e3},
        {'mode': 'ACI', 'mrange': 3, 'value': 2, 'frequency': 5e3},

        # Frequency verification points
        {'mode': 'FREQ', 'mrange': 10, 'value': 5, 'frequency': 10},
        {'mode': 'FREQ', 'mrange': 10, 'value': 5, 'frequency': 1e3},
        {'mode': 'FREQ', 'mrange': 10, 'value': 5, 'frequency': 10e3},
        {'mode': 'FREQ', 'mrange': 10, 'value': 5, 'frequency': 100e3},
        {'mode': 'FREQ', 'mrange': 10, 'value': 5, 'frequency': 300e3},

    ]

    # Keithley/Tek recommended verification points
    cal3 = [

        # 4W resistance verification points
        {'mode': 'OHM4W', 'mrange': 10e6,  'value': 0,     'frequency': 0},
        {'mode': 'OHM4W', 'mrange': 10e6,  'value': 10e6,  'frequency': 0},

        # 2W resistance recommended point from manual
        {'mode': 'OHM2W', 'mrange': 100e6, 'value': 0,      'frequency': 0},
        {'mode': 'OHM2W', 'mrange': 100e6, 'value': 100e6,  'frequency': 0},

    ]


    callist = [
        {
            'instruction': (
                "Connect the Fluke 5720A/5730A to the DMM6500 front terminals. "
                "For ACV 740 Vrms at 50 kHz / 100 kHz use the 5725A amplifier. "
                "For low-level DCI (10 uA to 100 mA), Keithley recommends a reference DMM "
                "in series for limit calculation."
            ),
            'calpoints': cal2,
            'calibrator in use': True
        }
    ]


    def init(self):
        self.set_timeout(10)
        self.idstr = self.query("*IDN?").strip()
        self.calstr = "--" #No CalStr available on Keithley 6500
        self.mode = None
        self.mrange = None

    def default_VISA(self):
        return 'TCPIP::192.168.2.88::INSTR'

    def __autozero(self, enabled, function=None):
        state = "ON" if enabled else "OFF"
        if function == "DCV":
            self.write(f":SENS:VOLT:DC:AZER {state}")
        elif function == "DCI":
            self.write(f":SENS:CURR:DC:AZER {state}")
        elif function == "OHM2W":
            self.write(f":SENS:RES:AZER {state}")
        elif function == "OHM4W":
            self.write(f":SENS:FRES:AZER {state}")
        else:
            self.write(f":SENS:AZER {state}")

    def __hiz(self, enabled):
        if enabled:
            self.write(":SENS:VOLT:INP AUTO")
        else:
            self.write(":SENS:VOLT:INP MOHM10")

    def __set_func(self, func):
        self.write(f':SENS:FUNC "{func}"')

    def __conf_range(self, func_path: str, mrange):
        if mrange is None:
            self.write(f":SENS:{func_path}:RANG:AUTO ON")
        else:
            self.write(f":SENS:{func_path}:RANG:AUTO OFF")
            self.write(f":SENS:{func_path}:RANG {mrange:0.6f}")

    def get_reading(self, channel=1):
        return float(self.query("READ?"))

    def trigger_read(self):
        self.write("INIT")

    def get_triggered_read(self):
        return float(self.query("FETCH?"))

    def conf_function_DCV(self, mrange=None, nplc=10, AutoZero=True, HiZ=True, channel=1):
        self.__set_func("VOLT:DC")
        self.__conf_range("VOLT:DC", mrange)
        self.write(f":SENS:VOLT:DC:NPLC {float(nplc):0.3f}")
        self.__autozero(AutoZero, "DCV")
        self.__hiz(HiZ)
        self.mode = 'DCV'
        self.mrange = mrange

    def conf_function_DCI(self, mrange=None, nplc=10, AutoZero=True, HiZ=True, channel=1):
        self.__set_func("CURR:DC")
        self.__conf_range("CURR:DC", mrange)
        self.write(f":SENS:CURR:DC:NPLC {float(nplc):0.3f}")
        self.__autozero(AutoZero, "DCI")
        self.mode = 'DCI'
        self.mrange = mrange

    def conf_function_ACV(self, mrange=None, nplc=None, AutoZero=True, HiZ=True, filter=30, channel=1):
        self.__set_func("VOLT:AC")
        self.__conf_range("VOLT:AC", mrange)
        self.__hiz(HiZ)
        self.write(f":SENS:VOLT:AC:DET:BAND {int(filter)}")
        self.mode = 'ACV'
        self.mrange = mrange

    def conf_function_ACI(self, mrange=None, nplc=None, AutoZero=True, HiZ=True, filter=30, channel=1):
        self.__set_func("CURR:AC")
        self.__conf_range("CURR:AC", mrange)
        self.write(f":SENS:CURR:AC:DET:BAND {int(filter)}")
        self.mode = 'ACI'
        self.mrange = mrange

    def conf_function_OHM2W(self, mrange=None, nplc=10, AutoZero=True, OffsetCompensation=False, channel=1):
        #no Offset Compensation in 2W Mode
        self.__set_func("RES")
        self.__conf_range("RES", mrange)       
        self.write(f":SENS:RES:NPLC {float(nplc):0.3f}")
        self.__autozero(AutoZero, "OHM2W")
        self.write(f":SENS:RES:OCOM {'ON' if OffsetCompensation else 'OFF'}")
        self.mode = 'OHM2W'
        self.mrange = mrange
        

    def conf_function_OHM4W(self, mrange=None, nplc=10, AutoZero=True, OffsetCompensation=True, channel=1):
        self.__set_func("FRES")
        self.write(f":SENS:FRES:OCOM OFF")
        self.__conf_range("FRES", mrange) #set range first, to allow of OffsetCompensation, if the meter was set on a higher range
        
        if mrange <= 10e3 and OffsetCompensation: #Offsetcompensation not available > 10kOhm
            self.write(f":SENS:FRES:OCOM ON")
            
        self.write(f":SENS:FRES:NPLC {float(nplc):0.3f}")
        self.__autozero(AutoZero, "OHM4W")
        self.mode = 'OHM4W'
        self.mrange = mrange

    def conf_function_FREQ(self, mrange=None, nplc=None, AutoZero=True, HiZ=True, filter=3, channel=1):
        self.__set_func("FREQ")
        # threshold range in the manual verification is set to 10 V
        if mrange is None:
            self.write(":SENS:FREQ:THR:RANG 10")
        else:
            self.write(f":SENS:FREQ:THR:RANG {float(mrange):0.6f}")
        self.write(":SENS:FREQ:APER 0.25")
        self.mode = 'FREQ'
        self.mrange = mrange

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

        raise ValueError(f"Mode not supported: {mode}")
