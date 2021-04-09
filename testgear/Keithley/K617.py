import testgear.base_classes as base

class K617(base.meter):
    def init(self):
        self.write("G1X") #switch prefix off


    def get_reading(self, channel=1):
        return float(self.read())


    def set_function(self, function, range=None, autorange=True):
        if function == "DCV":
            self.write("F0X")
        elif function == "DCA":
            self.write("F1X")
        elif function == "OHMS":
            self.write("F2X")
        elif function == "CHARGE":
            self.write("F3X")
        elif function == "external feedback":
            self.write("F4X")
        elif function == "V/I OHMS":
            self.write("F5X")


    def get_status(self):
        return self.query("U0X")


    def set_output(self, voltage=None, current=None, enabled=True):
        """set internal voltage source. current isn't supported"""
        if enabled == True:
            self.write("O1X")
        else:
            self.write("O0X")
    
        if voltage is not None:
            self.write("V{0:0.2f}X".format(voltage))


    def get_output(self):
        """returns set values: voltage, current, output state"""
        return np.nan, np.nan, False
