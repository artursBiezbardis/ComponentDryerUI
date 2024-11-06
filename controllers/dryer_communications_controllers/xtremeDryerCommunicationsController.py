from services.dryer_communication_services.xtremeDryerCommunicationsService import XtremeDryerCommunicationsService


class XtremeDryerCommunicationsController:

    def main(self) -> list:

        result = XtremeDryerCommunicationsService().main()

        return result
