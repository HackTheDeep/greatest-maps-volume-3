#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

host = os.getenv('es')
es = Elasticsearch(hosts = host)

def push_to_elasticsearch(obj):

    try:
        bulk(client = es, index = obj.get('index_name'), doc_type = 'docs', actions = obj.get('body'))
    except Exception as e:
        print(e)

def open_json(file_):
    index_name = (file_.split('.json')[0].split('/')[-1].lower())
    with open(file_) as f:
        body = json.load(f)
    obj = {
             'index_name': index_name,
             'body' : body,
             }
    return obj

def main():
    json_dir = '../../jsons/'
    file_list = os.listdir(json_dir)
    json_list = [j for j in file_list if j.endswith('.json')]
    for file_ in json_list:
        json_obj = open_json(json_dir + json_list[0])
        push_to_elasticsearch(json_obj)

if __name__ == "__main__":
    main()
    
