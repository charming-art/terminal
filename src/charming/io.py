import json
import csv
from functools import reduce


def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        return json.load(fp)


def load_csv(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        rows = list(csv.reader(fp))
        keys = rows[0]
        os = []
        for source in rows[1:]:
            o = {}
            for i, key in enumerate(keys):
                o[key] = source[i]
            os.append(o)
        return os
