from config import BARCODE_SETTINGS


class RegexUtilities:

    def create_item_barcode_regex_pattern(self):

        return self._create_carrier_barcode_regex()+"|"+self._create_custom_barcode_regex()

    @staticmethod
    def _create_carrier_barcode_regex():
        carrier_first_chars = BARCODE_SETTINGS['allowed_first_char_carrier_barcode']
        carrier_digit_count = BARCODE_SETTINGS['allowed_count_of_digits_carrier_barcode']

        regex_init = r"^["

        for char in carrier_first_chars:
            regex_init += char
        regex_init += "]\\"
        regex_init += "d{"+str(carrier_digit_count)+"}$"
        return regex_init


    @staticmethod
    def _create_custom_barcode_regex():
        custom_first_chars = BARCODE_SETTINGS['allowed_first_char_custom_barcode']
        custom_digit_count = BARCODE_SETTINGS['allowed_count_of_digits_custom_barcode']
        regex_init = "^["
        for char in custom_first_chars:
            regex_init += char
        regex_init += "]\\"
        regex_init += "d{"+str(custom_digit_count)+"}$"
        return regex_init
