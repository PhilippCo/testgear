import testgear.base_classes as base

class DS2072(base.scope):
    def init(self):
        self.timebase = timebase_class(self.resource)


class timebase_class(base.instrument):
    def __init__(self, resource):
        self.resource = resource

    def hallo(self):
        print(self.query("*IDN?"))
