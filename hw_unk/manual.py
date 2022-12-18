class ManualCsvConverter:

    def __init__(self, csv_data):
        self.title = csv_data[0]
        self.values = csv_data[1:]
        

    def prepare_title(self):
        title = self.title.strip().split(',')
        return title
        

    def prepare_row_values(self):
        values = [row.strip().split(',') for row in self.values]
        return values


    def convert_row_to_json(self, data):
        formatted_values = ",\n  ".join(["""\"{}\": \"{}\"""".format(key, value) for key, value in data.items()])
        pretty_line = """{{{}}}""".format(formatted_values)
        return pretty_line


    def to_json(self):
        title = self.prepare_title()
        row_values = self.prepare_row_values()
        
        self.check_data(title, row_values)
        
        
        sorted_by_column = [row for row in sorted(zip(title, row_values[0], row_values[1], row_values[2]))]
        
        title = []
        row_values = []
        for i in range(len(sorted_by_column[0])):
            if i == 0:
                for j in range(len(sorted_by_column)):
                    title.append(sorted_by_column[j][0])
            else:
                row = []
                for j in range(len(sorted_by_column)):
                    row.append(sorted_by_column[j][i])
                row_values.append(row)

        result = [self.convert_row_to_json(dict(zip(title, row))) for row in row_values]
        return "[{}]".format(",\n ".join(result))
     
       
    def check_data(self, title, row_values):
        for row in row_values:
            assert len(title) == len(row), "Column count is not equals value count"