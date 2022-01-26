import json
import yaml
import os

JSON_EXTENSION = ['.json']
YAML_EXTENSION = ['.yml', '.yaml']


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


def get_structure(file_path):
    with open(file_path, 'r') as file:
        file_extension = os.path.splitext(file_path)[1]
        if file_extension in JSON_EXTENSION:
            return json.load(file)
        if file_extension in YAML_EXTENSION:
            return yaml.safe_load(file)

    return {}


def generate_diff(first_file_path, second_file_path):
    first_data = get_structure(first_file_path)
    second_data = get_structure(second_file_path)

    new = second_data.copy()
    new.update(first_data)

    # for key, value in new.items():
    #     print('***')
    #     # print(key, '---', value)
    #     print(key, '---', first_json.setdefault(key, None))
    #     print(key, '---', second_json.setdefault(key, None))

    formated_line = []

    for key in new:
        formated_line.append((
            key,
            first_data.setdefault(key, None),
            second_data.setdefault(key, None)
        ))

    formated_line.sort()

    result = '{\n'
    for k, v1, v2 in formated_line:
        single_line = get_format_diff(k, v1, v2)
        result += single_line
    result += '}\n'

    # print('RESULT ==', result)

    return result
