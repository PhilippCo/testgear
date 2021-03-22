
import testgear.base_classes as base

class F5440B(base.calibrator):

    def output(self, state):
        if state:
            self.write("OPER")
        else:
            self.write("STBY")


