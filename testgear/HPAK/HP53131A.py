
import testgear.base_classes as base

class HP53131A(base.dmm):
    def get_reading(self, channel=None):
        return float(self.query("READ?").strip())


