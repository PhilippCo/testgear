
import testgear.base_classes as base

class HP53131A(base.meter):
    def init(self):
        self.write("*RST")
        self.idstr = self.query("*IDN?").strip()


    def get_reading(self, channel=None):
        """get frequency reading"""
        if channel == 1:
            self.write(':SENSe:FUNCtion "FREQUENCY 1"')
        elif channel == 2:
            self.write(':SENSe:FUNCtion "FREQUENCY 2"')

        return float(self.query("READ?").strip())


    def conf_function_frequency(self, gatetime=1, channel=1):
        self.write(":SENS:FREQ:ARM:STOP:SOUR TIM")
        self.write(":SENS:FREQ:ARM:STOP:TIM {0:0.3g}".format(gatetime))


    def set_gatetime(self, gatetime):
        pass


    def set_trigger_level(self, level):
        pass


    def set_100kHz_filter(self, state, channel=1):
        pass


    def set_DC_coupling(self, state, channel=1):
        pass




# counting

# initialize
# HP53131.write("*RST")
# HP53131.write(":CONF:TOTalize:CONT")

# start counting
# HP53131.write(":INITiate")

# one have to Abort the counting before one can fetch the data
# HP53131.write(":Abort")
# count = float(HP53131.query(":FETCH?"))
