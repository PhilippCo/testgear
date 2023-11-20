# Keithley 2470 Source Meter

# basic commands are compatible with Agilent B2902A Source Meter

import testgear.HPAK as HPAK

class K2470(HPAK.B2902A): 
    def default_VISA(self):
        return self.ip2visa("172.16.0.30")
