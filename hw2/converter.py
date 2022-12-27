import sys

def read_data(file_name):
    file = open(file_name)
    content = file.read()
    file.close()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()
    

def read_data(file_name):
    file = open(file_name)
    content = file.read()
    file.close()
    return content
    

def read_data_to_list(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    return content  


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)	
    file.close()
    
    
def prepare_data(data):
    title = data.pop(0).strip().split(',')
    return title, data


def convert_row_to_pretty_json(keys, row):
    values = row.strip().split(',')
    a = dict(zip(keys, values))
    
    return a


def convert_csv_to_json(input_path, output_path):
    try:
        data = read_data_to_list(input_path)
        title, data = prepare_data(data)

        if len(data) == 0:
            data = ["," * (len(title) - 1)]
            
        result = [convert_row_to_pretty_json(title, row) for row in data]  
        result = some_replaces_to_do_it_all(result)
    except:
        result = '[]'

    write_data(output_path, result)

def some_replaces_to_do_it_all(row):
	res = str(row).\
		replace('\'', '\"').\
		replace(', ', ',\n    ').\
		replace("{", "{\n        "). \
    	replace("}", "\n    }").\
    	replace("[", "[\n    ").\
    	replace("]", "\n]").\
    	replace("\",\n", "\",\n    ")
	return res
	
def main():
    args = sys.argv[1:]
    if len(args) < 2:
        args = ['input.csv', 'output.json']
    convert_csv_to_json(args[0], args[1])
	

if __name__ == "__main__":
    main()
