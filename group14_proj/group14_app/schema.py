class Create:

    def __init__(self, name, *args):
        self.create_table(name, *args)

    def create_table(self, name, *args):
        self.records = []
        self.table_schema = []
        self.name = name
        for arg in args:
            self.table_schema.append(arg)

    def show_attributes(self):
        for i in range(0, len(self.table_schema)):
            print(self.table_schema[i])

    def show_records(self):
        for i in self.records:
            print(i)

    def show_item(self, row_num: int = 0):
        if row_num < 0 or row_num >= len(self.records):
            raise TypeError(
                f'table only has {len(self.records)+1} records but {row_num}th records is requested')
        else:
            print(self.records[row_num])

    def get_records(self):
        return self.records

    def get_item(self, row_num: int = 0):
        if row_num < 0 or row_num >= len(self.records):
            raise TypeError(
                f'table only has {len(self.records)+1} records but {row_num}th records is requested')
        else:
            return self.records[row_num]
