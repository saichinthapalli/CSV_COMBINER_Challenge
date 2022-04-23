import sys
import os
import csv
import pandas as pd
class csv_combiner_1:
    def main(self, argv: list):
        combined_csv_file = pd.DataFrame()
        df = pd.DataFrame()
        if len(argv) <= 1:
            print(" Error: No or wrong file_paths input. Check your input file \n")
            return
        else:
            for file_path in argv[1:]:
                df = pd.read_csv(file_path, escapechar='\\')
                df['filename'] = os.path.basename(file_path)
                combined_csv_file = pd.concat([combined_csv_file, df])
                print(combined_csv_file.to_csv(index=False, header=True, line_terminator='\n', quoting = csv.QUOTE_NONE))
class csv_combiner_2:
    def main(self, argv: list):
        combined_csv_file = []
        df = []
        if len(argv) <= 1:
            print("Error: No or wrong file paths input. Check your input file")
            return
        else:
            for file_path in argv[1:]:
                for chunk in pd.read_csv(file_path, chunksize=100000, escapechar='\\'):
                    chunk['filename'] = os.path.basename(file_path)
                    combined_csv_file.append(chunk)
            header = True
            for chunk in combined_csv_file:
                print(chunk.to_csv(index=False, header=header, line_terminator='\n', chunksize=100000, quoting=csv.QUOTE_NONE), end='')
                header = False
total_size_file = 0
for file_path in sys.argv[1:]:
    size = os.path.getsize(file_path)
    total_size_file = size + total_size_file
if total_size_file <= 1.25 * 10**8:
    combined_csv_file = csv_combiner_1()
else:
    combined_csv_file = csv_combiner_2()
combined_csv_file.main(sys.argv)






