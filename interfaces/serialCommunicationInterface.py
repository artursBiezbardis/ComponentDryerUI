from abc import ABC, abstractmethod
# from controllers.dryer_communications_controllers.dryerCommunicationsController import DryerCommunicationsController


class SerialCommunicationInterface(ABC):

    @abstractmethod
    def request_data(self, communication_controller):
        pass

    @abstractmethod
    def receive_data(self, communication_controller):
        pass


