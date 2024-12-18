import utilities.CSVAndTSVUtilities as tsv
from database import AsyncSessionLocal
from models.models import CarrierData


class UpdateCarrierTable:

    async def add_carrier_table_data(self, carrier_table_path: str) -> None:
        """Updates the carrier table with data from the given TSV file."""
        async with AsyncSessionLocal() as db_session:

            tsv_data = tsv.CSVReader().read_tsv(carrier_table_path)
            header, *data_rows = tsv_data

            for row in data_rows:
                if row:
                    new_data = CarrierData(
                        carrier_id=str(row[0]),
                        part_name=row[1],
                        quantity=int(row[2]),
                        time_first_load=str(row[3]),
                        msl_time=int(row[4]),
                        pauses_total_time=float(row[5]),
                        part_height=int(row[7])
                    )
                    db_session.add(new_data)
            await db_session.commit()

    async def update_carrier_table(self, carrier_table_path: str) -> None:
        """Updates the carrier table with data from the given TSV file."""
        async with AsyncSessionLocal() as db_session:
            tsv_data = tsv.CSVReader().read_tsv(carrier_table_path)
            header, *data_rows = tsv_data

            for row in data_rows:
                if row:
                    new_data = CarrierData(
                        carrier_id=str(row[0]),
                        part_name=row[1],
                        quantity=int(row[2]),
                        time_first_load=str(row[3]),
                        msl_time=int(row[4]),
                        pauses_total_time=float(row[5]),
                        part_height=int(row[7])
                    )
                    db_session.add(new_data)
            await db_session.commit()



update = UpdateCarrierTable()


import asyncio
asyncio.run(update.update_carrier_table('../data/carrier_data.tsv'))