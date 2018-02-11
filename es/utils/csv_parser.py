#!/usr/bin/env python

import os
import codecs
import csv
import json
import pprint


def find_dupes(header_):
    dups = []
    dupers = []
    for h in header_:
        if h in dups:
            dupers.append(h)
            h += '_dupe'
        dups.append(h)
    return(dupers)

def write_file(file_, json_list):

    # Make sure to change the .csv to a .json
    file_name = file_.split('.csv')[0] + '.json'
    with open(file_name, 'w') as f:
        f.write(json.dumps(json_list))


def read_file(file_):
    with codecs.open(file_, 'r', 'latin1') as f:
        reader = csv.reader(f)
        header =  []
        json_list = []
        for e, row in enumerate(reader):
            if e == 0:
                header_ = row
                header = find_dupes(header_)
                continue
            row = [r for r in row]
            row_obj = {k:v for k,v in zip(header,row)}
            json_list.append(row_obj)

    return json_list

def main():
    file_dir = '../../csvs/'
    json_dir = '../../jsons/'
    file_list = os.listdir(file_dir)
    file_list = [f for f in file_list if f.endswith('.csv')]

    for f in file_list:
        json_list = read_file(file_dir + f)
        write_file(json_dir + f, json_list)

if __name__ == "__main__":
    main()
    
