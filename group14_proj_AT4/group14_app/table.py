from group14_app.schema import *


class Table:

    def __init__(self, table, row):
        self.add_record(table, row)

    def add_record(self, table, row):
        if len(row) != len(table.table_schema):
            raise TypeError(
                f'takes only {len(table.table_schema)} arguments but {len(row)} given')
        else:
            record = {}
            for col, index in zip(table.table_schema, range(0, len(table.table_schema))):
                record[col] = row[index]
            table.records.append(record)
