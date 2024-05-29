from services.msl_form_services.mslSelectionValuesService import MslSelectionValueService


class MslSelectionValueController:

    def main(self, thickness):
        if thickness == 'custom':
            return ['custom']
        else:
            return MslSelectionValueService().main(thickness)

