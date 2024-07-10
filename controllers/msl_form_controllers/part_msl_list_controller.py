from services.msl_form_services.partMSLListService import PartMSLListService


class PartMSLListController:

    def main(self, part_name):

        return PartMSLListService().main(part_name)
