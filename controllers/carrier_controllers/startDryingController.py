from services.carrier_services.startDryingService import StartDryingService


class StartDryingController:

    def main(self, item_data_template):
        start_drying = StartDryingService()
        start_drying.main(item_data_template)

