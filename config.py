SERIAL_SETTINGS = {
    'baud_rate': 9800,
    'timeout': 0.1,
    'port': '/dev/tty',
    'stack_light_red_on': 'RED',
    'stack_light_green_on': 'GREEN',
    'stack_light_yellow_on': 'YELLOW',
    'status_not_ready': 'S10',
    'status_ready': 'S11',
    'status_request': 'S1'
}

TIMER_SETTINGS = {
    'refresh_drying_list': 30,
    'dryer_status_request': 60
}

BARCODE_SETTINGS = {
    'allowed_first_char_carrier_barcode': ['r', 'R'],
    'allowed_count_of_digits_carrier_barcode': 6,
    'allowed_first_char_custom_barcode': ['c', 'C'],
    'allowed_count_of_digits_custom_barcode': 2,

    'allowed_first_chars_position_in_dryer': ['l', 'L'],
    'allowed_count_of_chars_position': 3


}

