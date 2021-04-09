
import testgear.base_classes as base

class A34970A(base.meter):
    def reset(self):
        self.write("*RST")
    
    def get_reading(self, channel=None):
        self.write("ROUT:SCAN (@{0:d})".format(channel))
        return self.query("READ?")


    def config_channel(self, meastype="VDC", range=None, autorange=True, nplc=20, ocomp=True ):
        pass


    def set_monitor_channel(self, channel):
        """selects which channel is displayed on the instrument (monitor)"""
        if not self.get_monitor_state():
            self.set_monitor_state(True)
        self.write("ROUTe:MONitor (@{0:d})".format(channel))


    def set_monitor_state(self, state):
        """switches the monitor on or off"""
        if state:
            self.write("ROUT:MON:STAT ON")
        else:
            self.write("ROUT:MON:STAT OFF")


    def get_monitor_state(self):
        """returns state of the monitor"""
        return bool(int(self.query("ROUT:MON:STAT?")))


    def set_relay(self, channel, state):
        """switches a relay on or off"""
        if state:
            self.write("ROUT:CLOSE (@{0:d})".format(channel))
        else:
            self.write("ROUT:OPEN (@{0:d})".format(channel))
