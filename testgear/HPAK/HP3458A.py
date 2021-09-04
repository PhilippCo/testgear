
import testgear.base_classes as base
import numpy as np
import struct

class HP3458A(base.meter):
    def init(self):
        self.write("END ALWAYS")

        self.idstr = self.query("ID?").strip()

        if "HP3458A" not in self.idstr:
            print("no HP3458A detected!!")
            return 1

        self.set_timeout(30)


    def cleanup(self):
        self.write("TRIG AUTO")


    def default_VISA(self):
        return 'TCPIP::192.168.2.88::gpib0,22::INSTR'


    def get_reading(self, channel=None):
        self.write("TRIG SGL") #Trigger reading
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

    
    def __ocomp(self, enabled=True):
        if enabled:
            self.write("OCOMP ON")
        else:
            self.write("OCOMP OFF")

  
    def conf_function_DCV(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.write("PRESET NORM")
        self.write("DCV")
        self.write("NDIG 8")
        self.write("TRIG SGL")
        self.__set_range(mrange, nplc)
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_DCI(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCI. if range=None the meter is set to Autorange"""
        self.write("PRESET NORM")
        self.write("DCI")
        self.write("NDIG 8")
        self.write("TRIG SGL")
        self.__set_range(mrange, nplc)
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_ACV(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.write("PRESET NORM")
        self.write("ACV")
        self.write("SETACV SYNC")
        self.write("NDIG 8")
        self.write("TRIG SGL")
        self.__set_range(mrange, nplc)
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_ACI(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.write("PRESET NORM")
        self.write("ACI")
        self.write("NDIG 8")
        self.write("TRIG SGL")
        self.__set_range(mrange, nplc)
        self.__autoZero(AutoZero)
        self.__hiZ(HiZ)


    def conf_function_OHM2W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        #TODO: Offsetcompensation
        self.write("PRESET NORM")
        self.write("OHM")
        self.write("NDIG 8")
        self.write("TRIG SGL")
        self.__set_range(mrange, nplc)
        self.__autoZero(AutoZero)
        self.__ocomp(OffsetCompensation)


    def conf_function_OHM4W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        #TODO: Offsetcompensation
        self.write("PRESET NORM")
        self.write("OHMF")
        self.write("NDIG 8")
        self.write("TRIG SGL")
        self.__set_range(mrange, nplc)
        self.__autoZero(AutoZero)
        self.__ocomp(OffsetCompensation)


    def read_samples(self, samplewidth=2, samples=2):
        """read samples in SINT (samplewidth=2) or DINT (samplewidth=4) format"""
        data   = self.resource.read_bytes(samplewidth*samples)
        chunks = [data[i:i+samplewidth] for i in range(0, len(data), samplewidth)]

        if samplewidth == 2:
            fstr = ">h"
        elif samplewidth == 4:
            fstr = ">i"
        else:
            print("format not supported!")

        unpacked = map(lambda a:struct.unpack(fstr, a)[0], chunks)
        
        arr  = np.fromiter(unpacked, float, count=samples)
        gain = float(self.query("ISCALE?"))
        return arr * gain


    def digitize(self, mrange=10, samples=512, srate=20e-6, aperture=3e-6, delay=0):
        #DCV digitizing
        #higher trigger jitter, but less noise
        #it doesn't use the sample&hold
        #bandwidth limited to 150kHz
        #max. sample rate 10µs (100kS/s)
        #Aperture 

        if srate < 10e-6:
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

        t = np.linspace(delay, samples*srate+delay, num=samples)
        return t, self.read_samples(samplewidth=2, samples=samples)


    def directsampling(self):
        #uses sample&hold
        #12MHz Bandwidth path
        #max 50kS/s
        #Aperture fixed 2ns (sample&hold)
        return np.array([]), np.array([])


    def subsampling(self, mrange=10, samples=500, srate=10e-9, delay=500e-9):
        #uses sample&hold
        #12MHz Bandwidth path
        #equivalent 100MS/s
        #Aperture fixed 2ns (sample&hold)

        self.write("PRESET FAST")#TARM SYN, TRIG AUTO, DINT FORMATS
        self.write("MEM FIFO")#ENABLE READING MEMORY, FIFO MODE
        self.write("MFORMAT SINT")#SINT READING MEMORY FORMAT
        self.write("OFORMAT SINT")
        self.write("SSDC 10")#SUB-SAMPLING, 10 V RANGE, LEVEL SYNC SOURCE EVENT (DEFAULT EVENT)
        self.write("SWEEP 10E-9,500")#4000 SAMPLES, 10 ns EFFECTIVE INTERVAL
        self.write("DELAY 500E-9")
        self.write("LEVEL 10 DC")#LEVEL TRIGGER AT 10% OF RANGE, DC-COUPLED
        self.write("SLOPE POS")#LEVEL TRIGGER ON POSITIVE SLOPE
        self.write("SSRC LEVEL")#LEVEL SYNC SOURCE EVENT
        self.write("TARM SGL")#ENABLE SAMPLING
        
        t = np.linspace(delay, samples*srate+delay, num=samples)
        return t, self.read_samples(samplewidth=2, samples=samples)