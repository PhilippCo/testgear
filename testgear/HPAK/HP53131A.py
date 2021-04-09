
import testgear.base_classes as base

class HP53131A(base.meter):
    def get_reading(self, channel=None):
        return float(self.query("READ?").strip())

    def set_gatetime(self, gatetime):
        pass

    def set_trigger_level(self, level):
        pass

    def set_100kHz_filter(self, state, channel=1):
        pass

    def set_DC_coupling(self, state, channel=1):
        pass




