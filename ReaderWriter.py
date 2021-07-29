import csv


class ReaderWriter:

    def __init__(self, name):
        self.name = name

    def reader(self):
        with open("phonebook_raw.csv", encoding="utf-8") as f:
            rows = csv.reader(f, delimiter=",")
            contacts_list = list(rows)
        return contacts_list

    def writer(self, well_done_list ):
        with open("phonebook_well_done.csv", "w", encoding='utf-8') as f:
            datawriter = csv.writer(f, delimiter=',')
            datawriter.writerows(well_done_list)