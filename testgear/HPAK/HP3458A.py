
import testgear.base_classes as base

class HP3458A(base.meter):
    def init(self):
        self.write("END ALWAYS")

        if "HP3458A" not in self.query("ID?"):
            print("no HP3458A detected!!")
            return 1

        self.set_timeout(30)

    

    def get_reading(self):
        return float(self.read())


    def display(self, text):
        self.write("DISP MSG {0:s}".format(text))


    def set_range(self, value=None, autorange=False):
        if autorange:
            self.write("RANGE AUTO")
        else:
            self.write("RANGE {0:d}".format(value))

    