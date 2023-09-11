from pathlib import Path

from classwork_2 import ui
from classwork_3 import get_from_user
from classwork_4 import csv_to_json
from homework import folder_info

if __name__ == '__main__':
    """запуск classwork_2"""
    ui()
    """запуск classwork_3"""
    get_from_user(Path('./data.json'))
    """запуск classwork_4"""
    csv_to_json(Path('data.csv'), Path('json_in.json'))
    """запуск homework"""
    folder_info(Path('C:/Users/dima4/python_basics/sem_8'))
