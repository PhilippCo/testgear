

import pyvisa
import numpy as np

class instrument:
    """This class abstracts pyvisa from all instruments"""

    rm = None #Class variable for pyvisa resource manager

    def __init__(self, visastr=None, gpib=None, gwip=None, ip=None):
        """open VISA instrument"""

        self.idstr = ""

        #create pyvisa instance if needed
        if instrument.rm == None:
            instrument.rm = pyvisa.ResourceManager('@py')
            #print("pyvisa initialized..")

        #gpib address given
        if gpib is not None:
            if gwip is not None:
                visastr = "TCPIP::{0:s}::gpib0,{1:d}::INSTR".format(gwip, gpib)
            else:
                visastr = "GPIB0::{0:d}::INSTR".format(gpib)

        #ip address given
        if ip is not None:
            visastr = "TCPIP::{0:s}::INSTR".format(ip)


        if visastr is None:
            visastr = self.default_VISA()

        if visastr is None: #check if VISA string is still None
            raise ValueError('Instrument Interface not defined!')

        self.resource = instrument.rm.open_resource(visastr)
        self.visastr  = visastr
        self.init() #call function to initialize instrument


    def default_VISA(self):
        """overload this method to define a default VISA string"""
        return None


    def __repr__(self):
        string = "============ Testgear Instrument ============\n"
        string += "Class:\t\t{}\n".format(type(self).__name__)
        string += "VISA String:\t{}\n".format(self.visastr)
        string += "ID String:\t{}\n".format(self.idstr)
        string += "Timeout:\t{0:0.3f} s\n".format(self.resource.timeout/1000)

        return string


    def is_type_of(self, insttype):
        """Check if class is of a specific type"""
        if type(self).__name__ == insttype:
            return True
        else:
            return False


    def set_timeout(self, timeout):
        """set instrument timeout in seconds"""
        self.resource.timeout = int(timeout * 1000)


    def init(self):
        """overload this method if initialization is needed"""
        pass


    def write(self, cmd):
        """write command to the instrument"""
        self.resource.write(cmd)


    def read(self):
        """read from instrument"""
        return self.resource.read()


    def query(self, cmd):
        """query instrument"""
        return self.resource.query(cmd)


    def cleanup(self):
        """overload this function to return the instrument to LOCAL"""
        pass


    def close(self):
        """close resource"""
        self.cleanup()
        self.resource.close()


    def __del__(self):
        self.close() #close instrument
        #print("Class {} destroyed".format(type(self).__name__))



class source(instrument):
    def set_output(self, voltage=None, current=None, enabled=True, frequency=0, resistance=None, fourWire=False, channel=1):
        #every source should have a set_output method
        pass

    def get_output(self):
        #every source should habe a get_output method
        obj = output_status()
        return obj


class meter(instrument):
    def read_avg(self, averages, channel=None):
        readings = []
        for _ in range(0, averages):
            readings.append(self.get_reading(channel=channel))
        
        return { "mean"    : np.mean(readings), 
                 "std"     : np.std(readings), 
                 "std_ppm" : np.std(readings)/np.mean(readings) * 1e6
               }


    def get_reading(self, channel=None):
        """returns the actual value"""
        return np.nan


    def conf_function_DCV(self, mrange=1000, nplc=200, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__not_supported()


    def conf_function_DCI(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCI. if range=None the meter is set to Autorange"""
        self.__not_supported()


    def conf_function_ACV(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__not_supported()


    def conf_function_ACI(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__not_supported()


    def conf_function_OHM2W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.__not_supported()


    def conf_function_OHM4W(self, mrange=None, nplc=200, AutoZero=True, OffsetCompensation=True, channel=1):
        """configures the meter to measure 4w resistance. if range=None the meter is set to Autorange"""
        self.__not_supported()


    def conf_function_frequency(self, gatetime=1, channel=1):
        self.__not_supported()


    def conf_function_count(self):
        self.__not_supported()


    def conf_function_period(self):
        self.__not_supported()

    #  HP 34401A
    #  FUNCtion "CONTinuity"
    #  FUNCtion "DIODe"
    #  FUNCtion "VOLTage:DC:RATio"

    #  HP 53131A
    # The <sensor_function> strings are:
    #???[:][XNONe:]DCYCle [1]???
    #or
    #???[:][XNONe:]PDUTycycle [1]???
    #???[:][XNONe:]FALL:TIME [1]???
    #or
    #???[:][XNONe:]FTIMe [1]???
    #???[:][XNONe:]FREQuency [1|2|3]???
    #???[:][XNONe:]FREQuency:RATio [ 1,2 | 1,3 | 2,1 | 3,1 ]???
    #???[:][XNONe:]NWIDth [1]???
    #???[:][XNONe:]PERiod [1|2|3]???
    #???[:][XNONe:]PHASe [1,2]???
    #???[:][XNONe:]PWIDth [1]???
    #???[:][XNONe:]TINTerval [1,2]???
    #???[:][XNONe:]TOTalize [1]???
    #???[:][XNONe:]RISE:TIME [1]???
    #or
    #???[:][XNONe:]RTIMe [1]???
    #???[:][XNONe:]VOLTage:MAXimum [1|2]???
    #???[:][XNONe:]VOLTage:MINimum [1|2]???
    #???[:][XNONe:]VOLTage:PTPeak [1|2]???

    def __not_supported(self):
        print("This function is not supported by {}".format(type(self).__name__))


class scope(instrument):
    pass


class output_status:
    """represents the output status of a channel"""
    def __init__(self):
        self.channel     = 1
        self.enabled     = False

        self.set_voltage = np.nan
        self.voltage     = np.nan
        
        self.set_current = np.nan
        self.current     = np.nan
        
        self.frequency   = 0
        self.waveform    = "DC"

        self.resistance  = np.nan

        self.uncertainty = np.nan


    def __repr__(self):
        string = "============ Channel {0:d} ============\n".format(self.channel)
        string += "enabled:\t{0}\n".format(self.enabled)
        string += "\n"
        string += "set_voltage:\t{0:0.6f} V\n".format(self.set_voltage)
        string += "set_current:\t{0:0.6f} A\n".format(self.set_current)
        string += "\n"
        string += "voltage:\t{0:0.6f} V\n".format(self.voltage)
        string += "current:\t{0:0.6f} A\n".format(self.current)
        string += "\n"
        string += "frequency:\t{0:0.6f} Hz\n".format(self.frequency)
        string += "waveform:\t{0:s}\n".format(self.waveform)
        string += "\n"
        string += "resistance:\t{0:0.6f} Ohm\n".format(self.resistance)
        return string



