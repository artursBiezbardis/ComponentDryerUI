from interfaces.serialCommunicationInterface import SerialCommunicationInterface
from controllers.dryer_communications_controllers.dryerCommunicationsController import DryerCommunicationsController
from config import SERIAL_SETTINGS


class StatusCommunicator(SerialCommunicationInterface):

    def __init__(self):

        self.request = SERIAL_SETTINGS['status_request']
        self.status_ready = SERIAL_SETTINGS['status_ready']
        self.receive = True

    def request_data(self, communication_controller: DryerCommunicationsController):
        communication_controller.dryer_communication.request(self.request)

    def receive_data(self, communication_controller: DryerCommunicationsController):
        status = communication_controller.dryer_communication.receive_data()

        return self.convert_status_to_bool(status)

    def convert_status_to_bool(self, status):
        result = False
        if status:
            if status == self.status_ready:
                result = True

        return result


class RedLightCommunicator(SerialCommunicationInterface):

    def __init__(self):
        self.request = SERIAL_SETTINGS['stack_light_red_on']
        self.receive = True

    def request_data(self, communication_controller: DryerCommunicationsController):
        communication_controller.dryer_communication.request(self.request)

    def receive_data(self, communication_controller: DryerCommunicationsController):
        pass


class YellowLightCommunicator(SerialCommunicationInterface):

    def __init__(self):
        self.request = SERIAL_SETTINGS['stack_light_yellow_on']
        self.receive = True

    @property
    def request(self) -> str:
        return self.request

    @request.setter
    def request(self, value):
        self._request = value

    @property
    def receive(self) -> bool:
        return self.receive

    @receive.setter
    def receive(self, value):
        self._receive = value

    def request_data(self, communication_controller: DryerCommunicationsController):
        pass

    def receive_data(self, communication_controller: DryerCommunicationsController):
        pass


class GreenLightCommunicator(SerialCommunicationInterface):

    def __init__(self):
        self.request = SERIAL_SETTINGS['stack_light_green_on']
        self.receive = True

    @property
    def request(self) -> str:
        return self.request

    @request.setter
    def request(self, value):
        self._request = value

    @property
    def receive(self) -> bool:
        return self.receive

    @receive.setter
    def receive(self, value):
        self._receive = value

    def request_data(self, communication_controller: DryerCommunicationsController):
        pass

    def receive_data(self, communication_controller: DryerCommunicationsController):
        pass

