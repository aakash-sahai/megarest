import falcon
from megapy import ArduinoConnection
from pin import PinResource
# from stepper import StepperResource
# from pushbutton import PushButtonResource

class MegaRestAPI(falcon.API):

    def __init__(self):
        falcon.API.__init__(self)
        self.connection = ArduinoConnection()

        pr = PinResource(self.connection)
        self.add_route('/api/pin', pr)
        self.add_route('/api/pin/{name}', pr)
        # self.add_route('/api/pushbutton/{name}', PushButtonResource(self.connection))
        # self.add_route('/api/stepper/{name}', StepperResource(self.connection))
