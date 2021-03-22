

import pyvisa
import numpy as np

class instrument:
    """This class abstracts pyvisa from all instruments"""

    rm = None #Class variable for pyvisa resource manager

    def __init__(self, visastr):
        """open VISA instrument"""

        #create pyvisa instance if needed
        if instrument.rm == None:
            instrument.rm = pyvisa.ResourceManager('@py')
            print("pyvisa initialized..")

        self.resource = instrument.rm.open_resource(visastr)
        self.init() #call function to initialize instrument

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


class scanner(instrument):
    pass


class dmm(instrument):
    
    def set_range(self, value=0, autorange=False):
        """sets the correct range for the given value"""
        pass

    def get_value(self):
        """returns the actual value"""
        return np.nan


    