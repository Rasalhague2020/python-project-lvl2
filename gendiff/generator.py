import os

import json


def get_format_diff(key, value_1, value_2):
    if (value_1 != None) and (value_2 != None):
        return f'- {value_1}\n+ {value_2}\n'
    if (value_1 != None) and (value_2 == None):
        return f'- {value_1}\n'


def get_gendiff(first_file_path, second_file_path):
    # print("It's two files: ", ff, " -- " , sf)

    first_json = json.load(open(first_file_path))
    second_json = json.load(open(second_file_path))

    print(first_json)
    print(second_json)

    result = '{\n'
    for key in first_json:
        formated_line = get_format_diff(
            key, first_json(key), second_json.setdefault(key, None)
        )
        # formated_line += '\n'
        result += formated_line

    return result


        # if key in second_json:
        #     get_str_diff(key, first_json.pop(key), second_json.pop(key))
        # else:
        #     get_str_diff(key, first_json.po(key), None)

