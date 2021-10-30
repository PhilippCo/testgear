import testgear.base_classes as base
import numpy as np
import time

class dummy_resource():
    def __init__(self):
        self.timeout = 1000


class dummy(base.meter):
    def __init__(self, visastr=None, gpib=None, gwip=None, ip=None, serial=None):
        self.idstr = "dummy instrument"

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
            visastr = "----"

        self.visastr = visastr
        
        self.resource = dummy_resource()
        self.nplc = 100
        self.mrange = 10

    def write(self):
        pass


    def read(self):
        return "3482"


    def query(self):
        return "123.4"

    
    def conf_function_DCV(self, mrange=None, nplc=200, AutoZero=True, HiZ=True, channel=None):
        self.mrange = mrange
        self.nplc   = nplc


    def get_reading(self, channel=None):
        time.sleep(self.nplc * 2 * 20e-3)
        if self.mrange is not None:
            mrange = self.mrange
        else:
            mrange = 0.5

        return np.random.normal(loc=mrange, scale=mrange*10e-6, size=None)


    
    def set_output(self, voltage=None, current=None, enabled=True, frequency=0, resistance=None, fourWire=False, channel=1):
        #every source should have a set_output method
        pass


    def get_output(self):
        #every source should habe a get_output method
        obj = base.output_status()
        return obj