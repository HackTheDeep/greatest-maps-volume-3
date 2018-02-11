#!/usr/bin/env python

import os
import codecs
import csv
import json
import pprint


class CsvMapper:

    def __init__(self, file_):
        self.file = file_
        self.file_location = '../../csvs/'
        self.json_location = '../../jsons/'
        self.cfile = self.file_location + self.file
        self.jfile = self.json_location + self.file.replace('csv', 'json')
        self.run()

    def run(self):
        rf = self.read_file()
        po = self.parse_object(rf)
        self.write_file(po)

    def find_dupes(self, header_):
        dups = []
        dupers = []
        for h in header_:
            if h in dups:
                dupers.append(h)
                h += '_dupe'
            dups.append(h)
        return(dups)

    def parse_object(self, obj):
        return obj

    def read_file(self):
        with codecs.open(self.cfile, 'r', 'latin1') as f:
            reader = csv.reader(f)
            header =  []
            json_list = []
            for e, row in enumerate(reader):
                if e == 0:
                    header_ = row
                    header = self.find_dupes(header_)
                    continue
                if e > 10:
                    break
                row_obj = {k:v for k,v in zip(header,row)}
                row_obj = self.sanitize_data(row_obj)
                json_list.append(row_obj)

        return json_list

    def sanitize_data(self, obj):
        san_obj = {k:v for k, v in obj.items() if v != ""}
        return san_obj

    def write_file(self, json_list):

        # Make sure to change the .csv to a .json
        file_name = self.jfile
        with open(file_name, 'w') as f:
            f.write(json.dumps(json_list))

class SimpleCsvParser(CsvMapper):

    def parse_object(self, obj):
        new_obj = obj
        return new_obj

def main():
    file_dir = '../../csvs/'
    file_list = os.listdir(file_dir)
    file_list = [f for f in file_list if f.endswith('.csv')]
    for f in file_list:
        print('Reading File: {}'.format(f))
        smapper = SimpleCsvParser(f)

if __name__ == "__main__":
    main()
