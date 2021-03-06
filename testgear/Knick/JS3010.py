"""Knick JS3010 Voltage and Current Calibrator"""

import testgear.base_classes as base
import numpy as np

class JS3010(base.source):
    def init(self):
        self.set_voltage = 0
        self.set_current = 0

        output = self.get_output()
        self.set_voltage = output.set_voltage
        self.set_current = output.set_current


    def default_VISA(self):
        return 'TCPIP::192.168.2.88::gpib0,11::INSTR'


    def set_output(self, voltage=None, current=None, enabled=True, frequency=None, resistance=None, channel=1):
        """
        configures the output of the Knick JS3010 calibrator
        voltage sets the output voltage in volt
        current sets the output current in amps
        if both are given (voltage and current) the voltage is used
        
        enabled enables or disables the calibrator output
        
        frequency not supported
        resistance not supported
        channel not supported"""
        output = self.get_output()

        if voltage is not None:
            if output.set_voltage is np.nan:
                self.write("P MODE V")
            self.write("X OUT {0:0.7g}".format(voltage))
                
        elif current is not None: #if both are given only voltage will be applied
            if output.set_current is np.nan:
                self.write("P MODE A")
            self.write("X OUT {0:0.7g}".format(current))


        if enabled:
            output = self.get_output()

            if output.enabled == False: #output is off and needs to be switched back on
                if output.set_voltage is not np.nan:
                    self.set_output(voltage=self.set_voltage)
                else:
                    self.set_output(current=self.set_current)

            self.set_voltage = output.set_voltage
            self.set_current = output.set_current

        else:
            self.write("Z")


    
    def get_output(self, channel=1):
        """return an object which reflects the output conditions"""
        obj = base.output_status()

        mode     = self.query("R MODE").strip()
        setvalue = float(self.query("R OUT").strip()[3:-1])

        if mode == "MODE A":
            obj.set_voltage = np.nan
            obj.set_current = setvalue
        else:
            obj.set_voltage = setvalue
            obj.set_current = np.nan

        if setvalue == 0:
            obj.enabled     = False
            obj.set_voltage = self.set_voltage
            obj.set_current = self.set_current
        else:
            obj.enabled = True

        return obj







    