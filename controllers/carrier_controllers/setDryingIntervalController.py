from services.carrier_services.setDryingIntervalService import SetDryingIntervalService


class SetDryingIntervalController:

    def main(self, thickness_level, moisture_level, hours_greater_or_less_than_72):
        return SetDryingIntervalService().main(thickness_level, moisture_level, hours_greater_or_less_than_72)
