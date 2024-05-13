import csv
from models.models import MslData, Session


def import_csv_to_db(csv_file_path):
    session = Session()
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')

        for row in csvreader:
            if row:  # Make sure the row is not empty
                new_data = MslData(
                    thickness_level=row[0],
                    moisture_level=row[1],
                    hours_greater_than_72=float(row[2]) if row[2] else None,
                    hours_less_than_72=float(row[3]) if row[3] else None
                )
                session.add(new_data)
        session.commit()


import_csv_to_db('../data/msl.csv')
