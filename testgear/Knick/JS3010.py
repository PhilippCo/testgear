

import testgear.base_classes as base

class JS3010(base.calibrator):

    output_value = 0 #stores the output to mimic an output switch

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
            return 'IDC'
        elif answer == "MODE V":
            return 'VDC'
        else:
            return "ERROR"


    def get_functions(self):
        return ['VDC', 'IDC']
    