# Keysight 34470A 7.5 digit DMM

import testgear.base_classes as base
import testgear.HPAK as HPAK
import numpy as np
class K34470A(HPAK.K34461A):

    def digitize_conf(self, mrange=10, samples=30000, srate=0, aperture=0, delay=0):
        self.write("*RST")
        self.write('CONF:VOLT:DC 10')
        self.write('SENS:VOLT:DC:NPLC 0.001')
        self.write('SENS:VOLT:DC:ZERO:AUTO 0')
        self.write('SENS:VOLT:DC:IMPEDANCE:AUTO ON')
        self.write('TRIG:SOUR INT')
        self.write('TRIG:SLOP POS')
        self.write('TRIG:DEL 0')
        self.write('TRIG:LEV 0')
        self.write('SAMP:SOUR TIM')
        self.write('SAMP:TIM MIN')
        self.write('SAMP:COUN '+str(samples))
        self.write('SAMP:COUN:PRET 250')


    def digitize_arm(self):
        self.write("INIT")


    def digitize_read(self):
        values    = list(map(float, self.query("FETCH?").split(",")))
        value_cnt = len(values)
        dt        = float(self.query('SAMP:TIM?'))
        t         = np.linspace(0, value_cnt * dt, value_cnt)
        return t, np.array(values)
