"""
Задание №1.
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдоименами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""


from pathlib import Path
from typing import TextIO
import json


def _read_or_begin(fd: TextIO) -> str:
    line = fd.readline()
    if not line:
        fd.seek(0)
        return _read_or_begin(fd)
    return line[:-1]


def two_files_in_one(numbers: Path, words: Path, result: Path) -> None:
    with (open(numbers, 'r', encoding='utf-8') as f_num,
          open(words, 'r', encoding='utf-8') as f_word,
          open(result, 'r', encoding='utf-8') as f_res
          ):
        len_numbers = sum(1 for _ in f_num)
        len_words = sum(1 for _ in f_word)
        for _ in range(max(len_numbers, len_words)):
            num = _read_or_begin(f_num)
            word = _read_or_begin(f_word)
            num_a, num_b = num.split('|')
            mult = int(num_a) * float(num_b)
            if mult < 0:
                f_res.write(f'{word.lower()} {abs(mult)}\n')
            elif mult > 0:
                f_res.write(f'{word.upper()} {round(mult)}\n')


def create_json(file: Path) -> None:
    file_data = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line.split()
            file_data[name.capitalize()] = float(number)
    with open(file.stem + '.json', 'w', encoding='utf-8') as f_2:
        json.dump(file_data, f_2, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    create_json(Path('../sem_7/res_classwork_3.txt'))
