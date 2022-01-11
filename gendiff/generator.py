import os

import json


def get_format_diff(key, value_1, value_2):
    if value_1 is None:
        return f'  + {key}: {value_2}'

    if value_2 is None:
        return f'  - {key}: {value_1}'

    if value_1 == value_2:
        return f'    {key}: {value_1}'

    return f'  - {key}: {value_1}\n  + {key}: {value_2}'

    # if (value_1 != None) and (value_2 != None):
    #     return f'- {value_1}\n+ {value_2}\n'

    # if (value_1 != None) and (value_2 == None):
    #     return f'- {value_1}\n'


def dict_trunct(source_dict, mask_dict):
    result = dict()

    for key in source_dict:
        if key not in mask_dict:
            result[key] = source_dict[key]

    return result


def get_gendiff(first_file_path, second_file_path):
    # print("It's two files: ", ff, " -- " , sf)

    first_json = json.load(open(first_file_path))
    second_json = json.load(open(second_file_path))

    new = second_json.copy()
    new.update(first_json)

    # print(first_json)
    # print(second_json)
    # print(new)

    # new_trunc = dict_trunct(new, first_json)
    # print(new_trunc)

    # new_trunc2 = dict_trunct(new, new_trunc)
    # print(new_trunc2)


    result = '{\n'
    # for key, value in new.items():
        # print('***')
        # print(key, '---', value)
        # print(key, '---', first_json.setdefault(key, None))
        # print(key, '---', second_json.setdefault(key, None))

    for key in new:
        formated_line = get_format_diff(
            key,
            first_json.setdefault(key, None),
            second_json.setdefault(key, None)
        )
        formated_line += '\n'
        result += formated_line

    result += '}\n'

    # for key, value in first_json.items():
    #     formated_line = get_format_diff(
    #         key, value, second_json.setdefault(key, None)
    #     )
    #     formated_line += '\n'
    #     result += formated_line
    # print(result)

    return result

