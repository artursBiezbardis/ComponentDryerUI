from view.app import DryerApp
import os

if __name__ == '__main__':
    try:
        if not os.path.exists('database.db'):
            raise ValueError('Upgrade database, run database upgrade scripts in database_upgrade_folder!')
    except ValueError as e:
        print(e)
        exit()
    DryerApp().run()
