import pyvisa
import numpy as np

class instrument:
    """This class abstracts pyvisa from all instruments"""

    rm          = None #Class variable for pyvisa resource manager
    instruments = []   #collect references to all instruments

    def __init__(self, visastr=None, gpib=None, gwip=None, ip=None, serial=None):
        """open VISA instrument"""
        instrument.instruments.append(self) #append to the list of instruments
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
            visastr = self.ip2visa(ip)

        if visastr is None: #if visastr is still None look for a default value
            visastr = self.default_VISA()

        if visastr is None: #check if VISA string is still None
            raise ValueError('Instrument Interface not defined!')

        self.resource = instrument.rm.open_resource(visastr)
        self.visastr  = visastr
        self.init() #call function to initialize instrument


    def trigger_all(self):
        """trigger all instrument instances"""
        for instance in instrument.instruments:
            instance.trigger()


    def trigger(self):
        """trigger a measurement - used to trigger multiple instruments at the same time"""
        print("Class {} wurde getriggert".format(type(self).__name__))


    def default_VISA(self):
        """overload this method to define a default VISA string"""
        return None


    def ip2visa(self, ip):
        """overload this method for SOCKET communication"""
        return "TCPIP::{0:s}::INSTR".format(ip)


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
        #ToDo: delete instrument from instruments list
        self.close() #close instrument
        #print("Class {} destroyed".format(type(self).__name__))



class source(instrument):
    def __init__(self, *args, **kwargs):

        if "set_output" not in dir(self):
            print("WARNING: set_output(self, voltage, current, enabled, frequency, resistance, fourWire, channel) needs to be implemented!")

        if "get_output" not in dir(self):
            print("WARNING: get_output(self) needs to be implemented!")

        super().__init__(*args, **kwargs)


    # def get_output(self):
    #     #every source should have a get_output method
    #     obj = output_status()
    #     return obj


class meter(instrument):
    def __init__(self, *args, **kwargs):

        if "get_reading" not in dir(self):
            print("WARNING: get_reading(self, channel) needs to be implemented!")

        super().__init__(*args, **kwargs)


    def read_avg(self, averages, channel=None):
        readings = []
        for _ in range(0, averages):
            readings.append(self.get_reading(channel=channel))
        
        return { "mean"    : np.mean(readings), 
                 "std"     : np.std(readings, ddof=1), 
                 "std_ppm" : np.std(readings, ddof=1)/np.mean(readings) * 1e6
               }


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



