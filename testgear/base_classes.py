

class instrument:
    def __init__(self, resource):
        self.resource = resource

    def close:
        self.resource.close()



class calibrator(instrument):      
    def output(self, state):
        print("not implemented!")

    def guard(self, state):
        pass

    def set_value(self, value):
        pass

    def get_value(self):
        return 0
    
    def set_function(self, function):
        pass

    def get_function(self):
        pass

    def get_functions(self):
        pass


class scanner(instrument):
    pass


class dmm(instrument):
    pass


    