"""Fluke 5730A Multifunction Calibrator"""

import testgear.base_classes as base
import numpy as np

class F5730A(base.source):

    def init(self):
        self.set_timeout(20)
        self.idstr = self.query("*IDN?").strip()

        idstring = self.idstr.split(",")
        if idstring[0] == "FLUKE" and idstring[1] == "5730A":
            print("Fluke 5730A calibrator detected")
        else:
            print("no Fluke 5730A detected!") #raise error?
        

    def set_output(self, voltage=None, current=None, enabled=True, frequency=0, resistance=None, fourWire=False, channel=1):
        if enabled:

            if voltage is not None:
                unit  = "V"
                value = voltage
            elif current is not None:
                unit  = "A"
                value = current
            elif resistance is not None:
                unit  = "OHM"
                value = resistance
                frequency = 0

            if fourWire:
                self.write("EXTSENSE ON")
            else:
                self.write("EXTSENSE OFF")

            self.write("OUT {0:0.6g}{1}, {2:0.6g}Hz;*CLS;OPER".format(value, unit, frequency))

        else: #not enabled
            self.write("STBY")
        
        self.__wait_for_settling()


    def __wait_for_settling(self):
        settled = False
        while not settled:
            isr = int(self.query("ISR?"))
            #print(isr)
            settled = bool(isr & 2**12) #Check for SETTLED Bit

    
    def get_cal_status(self):
        # CAL_DAYS? Returns the number of days elapsed since the last calibration activity of the specified type
        # CAL_INTV? Returns the calibration interval for main output calibration
        # ONTIME? Returns the time in minutes since the Calibrator was turned on
        return 0


    def set_time(self):
        '''sets the clock of the calibrator'''
        pass


    def guard(self, state):
        """Guard configuration:
            True -> Guard connected to LO
            False -> Guard disconnected from LO
        """
        if state:
            self.write("EXTGUARD OFF")
        else:
            self.write("EXTGUARD ON")


    def lock_range(self, state=False):
        """Locks the present output range"""
        if state:
            self.write("RANGELCK ON")
        else:
            self.write("RANGELCK OFF")


    def get_output(self):
        """return an object which reflects the output conditions"""
        obj = base.output_status()

        # CAL_CONF?  Returns the current calibration confidence level
        
        isr = int(self.query("ISR?")) # Calibrator status register
        obj.enabled = bool(isr & 0b1)

        output = self.query("ADJOUT?").split(",") #read adjusted value
        # example 1.883E-01,A,4.42E+02

        aset = self.query("OUT?").split(",") #read actual setpoint

        unc = self.query("UNCERT?").split(",") #read uncertainty
        obj.uncertainty = float(unc[0])

        if output[1] == "V":
            obj.set_voltage = float(aset[0])
            obj.voltage     = float(output[0])
            obj.frequency   = float(output[2])

        elif output[1] == "A":
            obj.set_current = float(aset[0])
            obj.current     = float(output[0])
            obj.frequency   = float(output[2])

        elif output[1] == "OHM":
            obj.resistance = float(output[0])
            obj.frequency  = 0

        else:
            print("no match!")


        if obj.frequency > 0:
            obj.waveform = "SINE"
        else:
            obj.waveform = "DC"

        return obj


    def cleanup(self):
        pass
        #self.write("LOCAL")
