
import testgear.base_classes as base

class setter():

    def ACV(self):
        pass

    def DCV(self):
        pass


class HP34401A(base.meter):
    def init(self):
        self.set = setter()

