import paho.mqtt.subscribe as subscribe

from dtc_controller import DtcController
from logger import get_logger


class Communication(object):
    def __init__(self):
        super(Communication, self).__init__()
        self.controller = DtcController()
        self.logger = get_logger()
        subscribe.callback(self.on_msg_receive, "/dtc", hostname="localhost")

    def on_clr_receive(self, _1, _2, _3):
        """
        Create clear topic if clients require it and use this callback.
        """
        self.logger.info("Received clear message")
        self.controller.clear_all_dtc()

    def on_get_all_receive(self):
        """
        Use this method to return the data if any clients need it.
        """
        self.logger.info("Received getAll message")
        return self.controller.read_all_dtc()

    def on_msg_receive(self, client, userdata, message):
        if not message:
            self.logger.info('Received empty message')
            return
        dtc = message.payload.decode()
        dtc = dtc.replace('"', '')
        self.logger.info('Received dtc "%s"' % dtc)
        if dtc:
            self.controller.raise_dtc(dtc)


if __name__ == '__main__':
    Communication()
