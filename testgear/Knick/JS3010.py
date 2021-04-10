"""Knick JS3010 Voltage and Current Calibrator"""

import testgear.base_classes as base

class JS3010(base.source):
    def set_output(self, voltage=None, current=None, enabled=True, frequency=None, resistance=None, channel=1):
        """set output. current isn't supported"""
        #implement automatic switching between voltage and current
        self.output(enabled)
        self.set_value(voltage)

    
    def get_output(self, channel=1):
        """return an object which reflects the output conditions"""
        obj = base.output_status()

        #obj.set_voltage = float(self.query("GOUT"))

        return obj


    #output_value = 0 #stores the output to mimic an output switch <- Klassenvariable?

    def init(self):
        self.output_value = self.get_value()


    def output(self, state):
        if state:
            self.set_value(self.output_value)
        else:
            self.write("Z")


    def guard(self, state):
        """Guard is not software controllable"""
        pass


    def div(self, state):
        """Divider is accessible via an additional connector"""
        pass


    def external_sense(self, state):
        """4W is done in hardware"""
        pass


    def set_value(self, value):
        """set output voltage"""
        self.output_value = value
        self.write("X OUT {0:0.7g}".format(value))


    def get_value(self):
        """get actual output value"""
        return float(self.query("R OUT").strip()[3:-1])


    def set_function(self, function):
        if function == "VDC":
            self.write("P MODE V")
        elif function == "IDC":
            self.write("P MODE A")


    def get_function(self):
        answer = self.query("R MODE")
        if answer == "MODE A":
            return 'DCA'
        elif answer == "MODE V":
            return 'DCV'
        else:
            return "ERROR"


    