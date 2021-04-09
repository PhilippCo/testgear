

import pyvisa
import numpy as np

class instrument:
    """This class abstracts pyvisa from all instruments"""

    rm = None #Class variable for pyvisa resource manager

    def __init__(self, visastr=None, gpib=None, gwip="192.168.2.88", ip=None):
        """open VISA instrument"""

        #create pyvisa instance if needed
        if instrument.rm == None:
            instrument.rm = pyvisa.ResourceManager('@py')
            print("pyvisa initialized..")

        #gpib address given
        if gpib is not None:
            if gwip is not None:
                visastr = "TCPIP::{0:s}::gpib0,{1:d}::INSTR".format(gwip, gpib)
            else:
                visastr = "GPIB0::{0:d}::INSTR".format(gpib)

        #ip address given
        if ip is not None:
            visastr = "TCPIP::{0:s}::INSTR".format(ip)

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



class source(instrument):
    pass


class meter(instrument):
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


class scope(instrument):
    pass


#diese Klasse zurückgeben bei get_output()
#dann get_output().voltage  um aktuelle Spannung zu lesen

class output_status:
    def __init__(self):
        self.enabled     = False

        self.set_voltage = np.nan
        self.voltage     = np.nan
        
        self.set_current = np.nan
        self.current     = np.nan
        
        self.frequency    = np.nan

        self.resistance  = np.nan

#ggf. property node zum setzen einiger werte nutzen
