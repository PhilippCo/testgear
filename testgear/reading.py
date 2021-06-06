import numpy as np

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
        
        for key in self.units:
            nom, denom = self.units[key]
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


