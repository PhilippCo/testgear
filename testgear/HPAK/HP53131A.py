
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
        self.set_timeout(gatetime +2)
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


    #  HP 53131A
    # The <sensor_function> strings are:
    #“[:][XNONe:]DCYCle [1]”
    #or
    #“[:][XNONe:]PDUTycycle [1]”
    #“[:][XNONe:]FALL:TIME [1]”
    #or
    #“[:][XNONe:]FTIMe [1]”
    #“[:][XNONe:]FREQuency [1|2|3]”
    #“[:][XNONe:]FREQuency:RATio [ 1,2 | 1,3 | 2,1 | 3,1 ]”
    #“[:][XNONe:]NWIDth [1]”
    #“[:][XNONe:]PERiod [1|2|3]”
    #“[:][XNONe:]PHASe [1,2]”
    #“[:][XNONe:]PWIDth [1]”
    #“[:][XNONe:]TINTerval [1,2]”
    #“[:][XNONe:]TOTalize [1]”
    #“[:][XNONe:]RISE:TIME [1]”
    #or
    #“[:][XNONe:]RTIMe [1]”
    #“[:][XNONe:]VOLTage:MAXimum [1|2]”
    #“[:][XNONe:]VOLTage:MINimum [1|2]”
    #“[:][XNONe:]VOLTage:PTPeak [1|2]”