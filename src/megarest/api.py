import falcon
from megapy import ArduinoConnection
from pin import PinResource
from pushbutton import PushButtonResource
from stepper import StepperResource
from device import DeviceResource

class MegaRestAPI(falcon.API):

    def __init__(self):
        falcon.API.__init__(self)
        ArduinoConnection.print_ttys()
        self.connection = ArduinoConnection()
        print("Auto selected device: " + str(self.connection.tty))

        pr = DeviceResource(self.connection)
        self.add_route('/api/device', pr)

        pr = PinResource(self.connection)
        self.add_route('/api/pin', pr)
        self.add_route('/api/pin/{name}', pr)
        self.add_route('/api/pin/{name}/{cmd}', pr)
        self.add_route('/api/pin/{name}/{cmd}/{arg}', pr)

        pbr = PushButtonResource(self.connection)
        self.add_route('/api/pushbutton', pbr)
        self.add_route('/api/pushbutton/{name}', pbr)
        self.add_route('/api/pushbutton/{name}/{cmd}', pbr)

        sr = StepperResource(self.connection)
        self.add_route('/api/stepper', sr)
        self.add_route('/api/stepper/{name}', sr)
        self.add_route('/api/stepper/{name}/{cmd}', sr)
        self.add_route('/api/stepper/{name}/{cmd}/{arg}', sr)
