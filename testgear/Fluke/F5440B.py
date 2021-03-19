
import testgear.base_classes as base

class F5440B(base.calibrator):

    def output(self, state):
        if state:
            self.resource.write("OPER")
        else:
            self.resource.write("STBY")
    