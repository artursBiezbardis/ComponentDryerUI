SERIAL_SETTINGS = {
    'baud_rate': 1200,
    'timeout': 0.1,
    'port': 'COM13',
    'stack_light_red_on': 'RED',
    'stack_light_green_on': 'GREEN',
    'stack_light_yellow_on': 'YELLOW',
    'status_not_ready': 'S10',
    'status_ready': 'S11',
    'status_request': 'S1'
}

TIMER_SETTINGS = {
    'refresh_drying_list': 30,
    'dryer_status_request': 60,
    'json_read_lower_offset': 2.7,
    'json_read_higher_offset': 3.1
}

DRYER_ENV_LIMITS = {
    'humidity_min': 0.6,
    'humidity_max': 0.6,
    'temp_min': 20.0,
    'temp_max': 20.0,
}

CONNECTION_TIMEOUT = {
    'connection_timeout_for_status': 90.0,
    'connection_timeout_for_alert_message': 3
}

BARCODE_SETTINGS = {
    'allowed_first_char_carrier_barcode': ['r', 'R'],
    'allowed_count_of_digits_carrier_barcode': 6,
    'allowed_first_char_custom_barcode': ['c', 'C'],
    'allowed_count_of_digits_custom_barcode': 2,

    'allowed_first_chars_position_in_dryer': ['l', 'L'],
    'allowed_count_of_chars_position': 3

}

COLORS = {
    'red_status': [0.96, 0.29, 0.25, 1],
    'green_status': [0.34, 0.59, 0.36, 1]
}
