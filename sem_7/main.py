from pathlib import Path
from classwork_1 import fill_numbers
from classwork_2 import aliases
from classwork_3 import from_two_files
from classwork_4 import make_files
from classwork_5 import new_make_file
from classwork_7 import sort_files
from homework_1 import group_rename


if __name__ == '__main__':

    fill_numbers(20, 'res_classwork_1.txt')

    aliases(10, 4, 7, Path('res_classwork_2.txt'))

    from_two_files(Path('res_classwork_1.txt'), Path('res_classwork_2.txt'), Path('res_classwork_3.txt'))

    make_files('bin', count=2)

    data = {'txt': 4, 'zip': 3}
    new_make_file(data)

    group_rename(4, 'bin', 'zip', [2, 4], "new")

    sort_files('Example_files')
