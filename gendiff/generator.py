import os

import json


def get_format_diff(key, value_1, value_2):
    if type(value_1) == bool:
        value_1 = str(value_1).lower()
    if type(value_2) == bool:
        value_2 = str(value_2).lower()

    if value_1 is None:
        return f'  + {key}: {value_2}\n'
    if value_2 is None:
        return f'  - {key}: {value_1}\n'
    if value_1 == value_2:
        return f'    {key}: {value_1}\n'

    return f'  - {key}: {value_1}\n  + {key}: {value_2}\n'


def dict_trunct(source_dict, mask_dict):
    result = dict()
    for key in source_dict:
        if key not in mask_dict:
            result[key] = source_dict[key]
    return result


def generate_diff(first_file_path, second_file_path):
    first_json = json.load(open(first_file_path))
    second_json = json.load(open(second_file_path))

    new = second_json.copy()
    new.update(first_json)

    # for key, value in new.items():
    #     print('***')
    #     # print(key, '---', value)
    #     print(key, '---', first_json.setdefault(key, None))
    #     print(key, '---', second_json.setdefault(key, None))

    formated_line = []

    for key in new:
        formated_line.append((
            key,
            first_json.setdefault(key, None),
            second_json.setdefault(key, None)
        ))

    formated_line.sort()

    result = '{\n'
    for k, v1, v2 in formated_line:
        single_line = get_format_diff(k, v1, v2)
        result += single_line
    result += '}\n'
    
    # print('RESULT ==', result)

    return result

