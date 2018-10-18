import falcon
import json
from megapy import DigitalPin, AnalogPin
from app import MegaRestApp
import traceback

class Exception400(Exception):

    def __init__(self, msg):
        Exception.__init__(self, msg)


class PinResource(object):
    pins = {}
    def __init__(self, conn):
        self.connection = conn

    def validate(self, req, resp, name):
        print "Received {} {} request with params {}".format(req.method, req.path, req.params)
        if name is None:
            raise Exception400("A pin name must be provided")
        elif name not in PinResource.pins:
            raise Exception400("Pin {} does not exist".format(name))

    def on_get(self, req, resp, name = None):
        try:
            self.validate(req, resp, name)
            resp.status = falcon.HTTP_200
            resp.media = { "error" : None, "value" : PinResource.pins[name].value }
        except Exception400 as ex:
            resp.status = falcon.HTTP_400
            resp.media = { "error" : str(ex) }
        except Exception as ex:
            resp.status = falcon.HTTP_500
            resp.media = { "error" : str(ex), "trace": traceback.format_exc() }

    def on_put(self, req, resp, name = None):
        try:
            self.validate(req, resp, name)
            value = req.media.get("value")
            if value is None:
                raise Exception400("Missing value")
            PinResource.pins[name].value = value
            resp.status = falcon.HTTP_200
            resp.media = { "error" : None }
        except Exception400 as ex:
            resp.status = falcon.HTTP_400
            resp.media = { "error" : str(ex) }
        except Exception as ex:
            resp.status = falcon.HTTP_500
            resp.media = { "error" : str(ex), "trace": traceback.format_exc() }


    def on_post(self, req, resp):
        print "Received {} {} request with params {}".format(req.method, req.path, req.params)

        try:
            type = req.media.get("type")
            pin = req.media.get("pin")
            mode = req.media.get("mode")
            thePin = None
            if pin is None:
                raise Exception400("A pin number must be provided")
            if type == "digital":
                if mode is None or mode not in [ "input", "output" ]:
                    raise Exception400("A mode ('input' | 'output') must be provided")
                thePin = DigitalPin(self.connection, pin, mode)
            elif type == "analog":
                thePin = AnalogPin(self.connection, pin)
            else:
                raise Exception400("Invalid type of pin: {}".format(type))
            PinResource.pins[thePin.name] = thePin
            resp.status = falcon.HTTP_200
            resp.media = { "error" : None, "name" : thePin.name }
        except Exception400 as ex:
            resp.status = falcon.HTTP_400
            resp.media = { "error" : str(ex) }
        except Exception as ex:
            resp.status = falcon.HTTP_500
            resp.media = { "error" : str(ex), "trace": traceback.format_exc() }
