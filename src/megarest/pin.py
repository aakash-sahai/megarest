import falcon
import json
from megapy import DigitalPin, AnalogPin
from app import MegaRestApp
import traceback

class PinResource(object):
    pins = {}
    def __init__(self, conn):
        self.connection = conn

    def on_get(self, req, resp, name = None):
        print "Received {} {} request with params {}".format(req.method, req.path, req.params)
        if name is None:
            resp.status = falcon.HTTP_400
            resp.media = { "error" : "A pin name must be provided" }
            return
        elif name not in PinResource.pins:
            resp.status = falcon.HTTP_400
            resp.media = { "error" : "Pin {} does not exist".format(name) }
            return
        try:
            resp.status = falcon.HTTP_200
            resp.media = { "value" : PinResource.pins[name].value }
        except Exception as ex:
            resp.status = falcon.HTTP_400
            resp.media = { "error" : str(ex), "trace": traceback.format_exc() }

    def on_put(self, req, resp, name = None):
        print "Received {} {} request with params {}".format(req.method, req.path, req.params)
        if name is None:
            resp.status = falcon.HTTP_400
            resp.media = { "error" : "A pin name must be provided" }
            return
        elif name not in PinResource.pins:
            resp.status = falcon.HTTP_400
            resp.media = { "error" : "Pin {} does not exist".format(name) }
            return

        try:
            value = req.media.get("value")
            resp.status = falcon.HTTP_200
            PinResource.pins[name].value = value
        except Exception as ex:
            resp.status = falcon.HTTP_400
            resp.media = { "error" : str(ex), "trace": traceback.format_exc() }
        resp.status = falcon.HTTP_200
        resp.media = { "value" : PinResource.pins[name].value }


    def on_post(self, req, resp):
        print "Received {} {} request with params {}".format(req.method, req.path, req.params)

        try:
            type = req.media.get("type")
            pin = req.media.get("pin")
            thePin = None

            if type == "digital":
                mode = req.media.get("mode")
                thePin = DigitalPin(self.connection, pin, mode)
            elif type == "analog":
                thePin = AnalogPin(self.connection, pin)
            else:
                raise Exception("Invalid type of pin: {}".format(type))
            PinResource.pins[thePin.name] = thePin
            resp.status = falcon.HTTP_200
            resp.media = { "name" : thePin.name }
        except Exception as ex:
            resp.status = falcon.HTTP_400
            resp.media = { "error" : str(ex), "trace": traceback.format_exc() }
