import csv

def add_to_csv(filename, row, new=False):
    mode = 'w' if new else 'a+'
    with (open(filename, mode=mode, newline='') as file):
        writer = csv.writer(file, delimiter=';')
        writer.writerow(row)