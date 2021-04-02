

import pyvisa
import numpy as np

class instrument:
    """This class abstracts pyvisa from all instruments"""

    rm = None #Class variable for pyvisa resource manager

    def __init__(self, visastr=None, gpib=None, ip="192.168.2.88"):
        """open VISA instrument"""

        #create pyvisa instance if needed
        if instrument.rm == None:
            instrument.rm = pyvisa.ResourceManager('@py')
            print("pyvisa initialized..")

        #build VISA string if not given
        if visastr == None:
            visastr = "TCPIP::{0:s}::gpib0,{1:d}::INSTR".format(ip, gpib)

        self.resource = instrument.rm.open_resource(visastr)
        self.init() #call function to initialize instrument

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

    def close(self):
        """close resource"""
        self.resource.close()



class calibrator(instrument):      
    def output(self, state):
        print("not implemented!")

    def guard(self, state):
        pass

    def external_sense(self, state):
        print("not implemented!")

    def set_value(self, value):
        pass

    def get_value(self):
        return np.nan
    
    def set_function(self, function):
        pass

    def get_function(self):
        return None

    def get_functions(self):
        return []

    def set_range(self, range):
        pass

    def get_range(self):
        return np.nan


class scanner(instrument):
    pass


class dmm(instrument):
    def read_avg(self, averages, channel=None):
        readings = []
        for _ in range(0, averages):
            readings.append(self.get_reading(channel=channel))
        return np.mean(readings), np.std(readings)


    def set_range(self, value=0, autorange=False):
        """sets the correct range for the given value"""
        pass

    def get_reading(self, channel=None):
        """returns the actual value"""
        return np.nan


class pwrsupply(instrument):
    pass


class siggen(instrument):
    pass
