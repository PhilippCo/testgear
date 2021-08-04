
import testgear.base_classes as base
import numpy as np
import struct

class HP3458A(base.meter):
    def init(self):
        self.write("END ALWAYS")
        self.write("NDIG 8")
        self.write("TRG SGL")

        self.idstr = self.query("ID?").strip()

        if "HP3458A" not in self.idstr:
            print("no HP3458A detected!!")
            return 1

        self.set_timeout(30)

    def cleanup(self):
        self.write("TRIG AUTO")


    def default_VISA(self):
        return 'TCPIP::192.168.2.88::gpib0,22::INSTR'


    def get_reading(self):
        self.write("TRG SGL") #Trigger reading
        return float(self.read())


    def display(self, text):
        self.write("DISP MSG {0:s}".format(text))

    
    def set_filter(self, enable=True):
        """low-pass filter with the -3dB point at 75kHz"""
        if enable:
            self.write("LFILTER ON")
        else:
            self.write("LFILTER OFF")


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
        self.write("PRESET NORM")
        self.write("DCV")
        self.__set_range(mrange, nplc)
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_DCI(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCI. if range=None the meter is set to Autorange"""
        self.write("PRESET NORM")
        self.write("DCI")
        self.__set_range(mrange, nplc)
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_ACV(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.write("PRESET NORM")
        self.write("ACV")
        self.__set_range(mrange, nplc)
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_ACI(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.write("PRESET NORM")
        self.write("ACI")
        self.__set_range(mrange, nplc)
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_OHM2W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.write("PRESET NORM")
        self.write("ACV")
        self.__set_range(mrange, nplc)
        self.__autoZero(AutoZero)


    def conf_function_OHM4W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.write("PRESET NORM")
        self.write("ACV")
        self.__set_range(mrange, nplc)
        self.__autoZero(AutoZero)


    def __unpack(self, arr):
        return struct.unpack(">h", arr)[0]


    def digitize(self, mrange=10, samples=512, srate=20e-6, aperture=3e-6, delay=0):
        if srate < 20e-6:
            print("Sample rate too high for digitzing, use subsampling!")
            return np.array([]), np.array([])

        self.write("PRESET DIG")
        # TARM HOLD -- Suspends triggering
        # TRIG LEVEL -- LEVEL trigger event
        # LEVEL 0,AC -- Level trigger at 0% of range (0 V), AC-coupled
        # TIMER 20E-6 -- 20 µs interval between samples
        # NRDGS 256,TIMER -- 256 samples per trigger, TIMER sample event
        # DCV 10 -- DC voltage measurements, 10 V range
        # DELAY 0 -- No delay
        # APER 3E-6 -- 3 µs integration time
        # MFORMAT SINT -- Single integer memory format
        # OFORMAT SINT -- Single integer output format
        # AZERO OFF -- Disables the autozero function
        # DISP OFF -- Disables the display

        self.write("DELAY {0:0.3g}".format(delay))
        self.write("MEM FIFO")
        self.write("NRDGS {0:d},TIMER".format(samples))

        self.write("TARM SYN")

        data = self.resource.read_bytes(2*samples) #für SINT
        info = [data[i:i+2] for i in range(0, len(data), 2)]
        arr  = np.array(list(map(self.__unpack, info)))
        gain = float(self.query("ISCALE?"))

        t = np.linspace(delay, samples*srate+delay, num=samples)
        return t, arr * gain


    def subsampling(self):
        pass