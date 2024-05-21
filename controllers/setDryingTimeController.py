from services.setDryingTimeService import SetDryingTimeService


class SetDryingTimeController:

    def main(self, thickness_level, moisture_level, hours_greater_or_less_than_72):

       return SetDryingTimeService().main(thickness_level, moisture_level, hours_greater_or_less_than_72)
