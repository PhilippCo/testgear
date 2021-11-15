import testgear.base_classes as base

class K617(base.meter):
    def init(self):
        self.write("G1X") #switch prefix off
        self.idstr = self.query("U0X")[:3]


    def get_reading(self, channel=1):
        return float(self.read())


    def set_special_function(self, function):
        #left this function to access the special functions (external feedback, V/I OHMS etc.)
        if function == "DCV":
            self.write("F0X")
        elif function == "DCI":
            self.write("F1X")
        elif function == "OHMS":
            self.write("F2X")
        elif function == "CHARGE":
            self.write("F3X")
        elif function == "external feedback":
            self.write("F4X")
        elif function == "V/I OHMS":
            self.write("F5X")

    
    def conf_function_DCV(self, mrange=1000, nplc=200, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.set_special_function("DCV")


    def conf_function_DCI(self, mrange=None, nplc=100, AutoZero=True, HiZ=True, channel=None):
        """configures the meter to measure DCI. if range=None the meter is set to Autorange"""
        self.set_special_function("DCI")


    def conf_function_OHM2W(self, mrange=None, nplc=100, AutoZero=True, OffsetCompensation=True, channel=None):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        self.set_special_function("OHMS")


    def get_status(self):
        return self.query("U0X")


    def set_output(self, voltage=None, current=None, enabled=True, frequency=0, resistance=None, fourWire=False, channel=1):
        """set internal voltage source. current isn't supported"""
        if enabled == True:
            self.write("O1X")
        else:
            self.write("O0X")
    
        if voltage is not None:
            self.write("V{0:0.2f}X".format(voltage))


    def get_output(self):
        """returns set values: voltage, current, output state"""
        obj = base.output_status()

        return obj
