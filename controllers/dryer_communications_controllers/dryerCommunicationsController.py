from repositories.dryer_communication_repositories.dryerCommunicationRepository import SerialManager
from interfaces.serialCommunicationInterface import SerialCommunicationInterface


class DryerCommunicationsController:

    def __init__(self, layout):
        self.dryer_communication = SerialManager(layout)
        self.serial_queue = False

    def main(self, communication_model: SerialCommunicationInterface):
        while self.serial_queue:
            pass
        self.serial_queue = True
        communication_model.request_data(self)
        result = communication_model.receive_data(self)
        connection = self.dryer_communication.connection
        connection.flush()
        connection.reset_input_buffer()
        connection.reset_output_buffer()
        self.serial_queue = False

        return result
