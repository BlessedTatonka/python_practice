import csv
import json
import sys

def convert_csv_to_json(input_path, output_path):
    res = []
      
    with open(input_path) as fin: 
        dr = csv.DictReader(fin) 

        for row in dr: 
            res.append(row)
  
    with open(output_path, 'w') as fout: 
        res = json.dumps(res, indent=4)
        fout.write(res)

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        args = ['input.csv', 'output.json']
    convert_csv_to_json(args[0], args[1])

if __name__ == "__main__":
    main()