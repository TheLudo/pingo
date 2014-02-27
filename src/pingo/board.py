
HIGH = 1
LOW = 0
INPUT = 0
OUTPUT = 1

class Board(object):
	pass

class Pin(object):

    def __init__(self, physical_pin, logical_pin=None):
        self.physical_pin = physical_pin
        if logical_pin is None:
            self.logical_pin = physical_pin
        else:
            self.logical_pin = logical_pin        

    def __repr__(self):
        return '<%s #%d>' % (
            self.__class__.__name__,
            self.physical_pin)

class GroundPin(Pin):
    pass

class VddPin(Pin):
    pass

class DigitalPin(Pin):

    def __init__(self, physical_pin, logical_pin=None, mode=OUTPUT, state=LOW):
        Pin.__init__(self, physical_pin, logical_pin)
        self.set_mode(mode)
        self.state = state

    def set_mode(self, mode):
        self.mode = mode

    def low(self):
        self.state = LOW

    def high(self):
        self.state = HIGH




INPUT = 0
OUTPUT = 1

