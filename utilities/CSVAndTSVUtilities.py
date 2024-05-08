import csv


class CSVReader:

    @staticmethod
    def read_tsv(file_path: str) -> list:
        data = []
        with open(file_path, 'r', encoding='utf-8') as tsvfile:
            reader = csv.reader(tsvfile, delimiter='\t')
            for row in reader:
                data.append(row)
        return data

