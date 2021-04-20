# HP 34970A 6.5 digit DMM with Multiplexer

import testgear.base_classes as base
import numpy as np

class A34970A(base.meter):
    def reset(self):
        self.write("*RST")
    

    def get_reading(self, channel=None):
        if channel in self.get_scanlist():
            if channel is not None:
                self.set_monitor_channel(channel)
            return float(self.query("ROUTe:MONitor:DATA?"))
        
        else:
            return np.nan


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
        state   = bool(int(self.query("ROUT:MON:STAT?")))
        channel = int(self.query("ROUTe:MONitor?").split("@")[1].split(")")[0])
        return channel, state


    def set_relay(self, channel, state):
        """switches a relay on or off"""
        if state:
            self.write("ROUT:CLOSE (@{0:d})".format(channel))
        else:
            self.write("ROUT:OPEN (@{0:d})".format(channel))


    def get_scanlist(self):
        data  = self.query("ROUTE:SCAN?")
        slist = data.split('@')[1].split(')')[0].split(',') 
        return set(map(int, slist))


    def trigger_scan(self):
        self.write("INIT")

    def get_triggered_scan(self):
        #gleiche Aufbereitung der Antwort wie in get_scan verwenden
        return self.query("FETCH?")


    def get_scan(self):
        #dictionary einbauen
        return self.query("READ?")


    def set_scanlist(self, slist:set):
        strlist = ""
        for chan in slist:
            strlist += "{0:d}, ".format(chan)
        self.write("ROUTE:SCAN (@{0:s})".format(strlist[:-2]))


    def clear_scanlist(self):
        self.write("ROUT:SCAN (@)")
        

    def conf_function_DCV(self, mrange=None, nplc=20, AutoZero=True, HiZ=True, channel=101):
        """configures the meter to measure DCV. if range=None the meter is set to Autorange"""
        slist = self.get_scanlist()
        slist.add(channel)

        self.write("CONF:VOLT:DC (@{0:d})".format(channel))
        
        if mrange is None:
            self.write("VOLT:DC:RANGE:AUTO 1,(@{0:d})".format(channel))
        else:
            self.write("VOLT:DC:RANGE {0:0.6f},(@{1:d})".format(mrange, channel))

        self.write("VOLT:DC:NPLC {0:0.3f},(@{1:d})".format(nplc, channel))
        
        #AutoZero
        #HiZ

        self.set_scanlist(slist)


    def conf_function_Pt100(self, mrange=None, nplc=20, fourWire=True, R0=100, channel=101):
        pass


#hp34970a.query("CONFigure?") zeigt Konfigurationen der Scanliste