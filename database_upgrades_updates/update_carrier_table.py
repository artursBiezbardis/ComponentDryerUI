import utilities.CSVAndTSVUtilities as tsv
from models.models import CarrierData, Session


def update_carrier_table(carrier_table_path):

    tsv_data = tsv.CSVReader().read_tsv(carrier_table_path)
    session = Session()
    del tsv_data[0]
    for row in tsv_data:
        if row:
            new_data = CarrierData(
                carrier_id=row[0],
                part_name=row[1],
            )
            session.add(new_data)
    session.commit()


update_carrier_table('../data/tabula.tsv')