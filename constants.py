ITEM_DATA_TEMPLATE = {'carrier_barcode': str(''),
                      'carrier_position': str(''),
                      'part_name': str(''),
                      'part_thickness': None,
                      'msl': None,
                      'hours_less_72_hours': False,
                      'hours_greater_than_72': False,
                      'drying_start_interval': None,
                      'add_interval': None,
                      'in_dryer': True,
                      'drying_finished': False,
                      'task_id': None,
                      'start_time': None,
                      'end_time': None,
                      'total_time': None,
                      'popup_opened': False,
                      'custom_part': False,
                      'auto_add_task': False,
                      'carrier_data': None

                      }
ADD_REM0VE_CARRIER = {'carrier_barcode': '',
                      'carrier_position': '',
                      'task_id': None,
                      'add_status': False,
                      'remove_status': False,
                      'status_message': '',
                      'alert_message': False,
                      'message_dismiss_button': False,
                      'message_ok_button': False,
                      'on_enter_recycle': False
                      }

MSL_EXPIRE = {0: 'msl 1', 365: 'msl 2', 28: 'msl 2a', 7: 'msl 3', 3: 'msl 4', 2: 'msl 5', 1: 'msl 5a'}
