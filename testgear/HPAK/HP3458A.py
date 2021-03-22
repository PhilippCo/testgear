
import testgear.base_classes as base

class HP3458A(base.dmm):
    
    def init(self):
        self.write("END ALWAYS")
    
