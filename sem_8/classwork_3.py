"""
Задание №3.
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
"""

import csv
import json
import os
from pathlib import Path


def get_from_user(file: Path) -> None:
    json_file = {}
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as js:
            if os.path.getsize(file) > 0:
                json_file = json.load(js)

    rows = []
    for level, value in json_file.items():
        for personal_id, name in value.items():
            rows.append({'level': level, 'personal_id': personal_id, 'name': name})

    with open('data.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['level', 'personal_id', 'name']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
