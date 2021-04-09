"""LakeShore 331 Temperature Controller"""

import testgear.base_classes as base

class LS331(base.instrument):
    
    def init(self):
        #configure LS331 control
        # 1 - loop 1
        # A - input A
        # 2 - unit in Celsius
        # 1 - powerup enable
        # 2 - show heater power
        self.write("CSET 1, A, 2, 1, 2")
        print(self.resource.query("*IDN?"))
        
    
    def check_inst(self):
        idn = self.query("*IDN?")
        if idn.split(",")[1] == "MODEL331S":
            return True
        else:
            return False
        
    def close(self):
        self.close()
    
    def set_temp(self, temperature):
        data = "SETP 1, {0:0.3f}".format(temperature)
        #print(data)
        self.write(data)
        
    def get_temp(self):
        return float(self.query("CRDG?"))
