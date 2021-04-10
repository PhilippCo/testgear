"""Knick JS3010 Voltage and Current Calibrator"""

import testgear.base_classes as base
import numpy as np

class JS3010(base.source):
    def init(self):
        output = self.get_output()
        self.set_voltage = output.set_voltage
        self.set_current = output.set_current


    def set_output(self, voltage=None, current=None, enabled=True, frequency=None, resistance=None, channel=1):
        """set output. current isn't supported"""
        #implement automatic switching between voltage and current
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


    #output_value = 0 #stores the output to mimic an output switch <- Klassenvariable?

    def guard(self, state):
        """Guard is not software controllable"""
        pass


    def div(self, state):
        """Divider is accessible via an additional connector"""
        pass


    def external_sense(self, state):
        """4W is done in hardware"""
        pass






    