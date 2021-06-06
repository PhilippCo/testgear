

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


        if visastr is None:
            visastr = self.default_VISA()

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
        string += "Timeout:\t{0:0.3f} s\n".format(self.resource.timeout/1000)

        return string


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



class reading:
    def __init__(self, value=np.nan, unit=None, unit_nom=None, unit_denom=None, channel=1):
        self.channel    = channel
        self.value      = value
        self.unit_nom   = unit_nom
        self.unit_denom = unit_denom
    
        self.units = { 
            "A"  : ( ["A"], [] ),
            "s"  : ( ["s"], [] ),
            "kg" : ( ["kg"], [] ),
            "m"  : ( ["m"], [] ),
            "K"  : ( ["K"], [] ),
            
            "V"   : ( ["kg", "m", "m"], ["A", "s", "s", "s"] ),
            "W"   : ( ["kg", "m", "m"], ["s", "s", "s"]),
            "Ohm" : ( ["kg", "m", "m"], ["A", "A", "s", "s", "s"]),
            "C"   : ( ["A", "s"], []),
            "Hz"  : ( [], ["s"])
        }
        
        if unit is not None:
            if unit in self.units:
                self.unit_nom, self.unit_denom = self.units[unit]
            else:
                print("unkown unit!")
        else:
            if unit_nom is None or unit_denom is None:
                print("a unit is needed!")
            else:
                self.unit_nom   = unit_nom
                self.unit_denom = unit_denom
        
        self.reduce()
    
    
    def reduce(self):
        """reduce fraction"""
        for symbol in self.unit_denom.copy():
            if symbol in self.unit_nom:
                self.unit_nom.remove(symbol)
                self.unit_denom.remove(symbol)
    
        
        
    def unit(self):
        """find derived unit"""
        snom   = sorted(self.unit_nom)
        sdenom = sorted(self.unit_denom)
        
        for key in a.units:
            nom, denom = a.units[key]
            if sorted(nom) == snom and sorted(denom) == sdenom:
                return key

            
        if len(self.unit_nom) == 0:
            unitstr = "1/({0})".format("*".join(self.unit_denom))
        elif len(self.unit_denom) == 0:
            unitstr = "{0}".format("*".join(self.unit_nom))
        else:
            unitstr = "({0})/({1})".format("*".join(self.unit_nom), "*".join(self.unit_denom))
        return unitstr
    
    
    def __truediv__(self, reading2):
        """divide two readings and divide the units by multiplying with the reciprocal"""
        nom   = self.unit_nom   + reading2.unit_denom
        denom = self.unit_denom + reading2.unit_nom
        
        result = reading(unit_nom=nom, unit_denom=denom)
        result.value = self.value / reading2.value
        result.reduce()
        return result

    
    def __mul__(self, reading2):
        """multiply two readings including units"""
        nom   = self.unit_nom   + reading2.unit_nom
        denom = self.unit_denom + reading2.unit_denom
        result = reading(unit_nom=nom, unit_denom=denom)
        result.value = self.value * reading2.value
        result.reduce()
        return result
   

    def __pow__(self, power):
        """power of reading"""
        #check for positive integer > 0

        #special case: power = -1 -> swap nom/denom and 1/value
        nom   = self.unit_nom * power
        denom = self.unit_denom * power
        result = reading(unit_nom=nom, unit_denom=denom)
        result.value = self.value**power
        result.reduce()
        return result

    

    def __repr__(self):          
        return "{0:0.3f} ".format(self.value) + self.unit()


