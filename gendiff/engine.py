import json
import os


def get_json_data(file_path):
    with open(os.path.abspath(file_path)) as f:
        return json.load(f)


def generate_diff(first_file, second_file):
    json_data1 = get_json_data(first_file)
    json_data2 = get_json_data(second_file)
    return get_diff(json_data1, json_data2)


def get_diff(data1, data2):
    temp = data2.copy()
    list_of_changes = ['{']

    for k, v in data1.items():
        new_v = temp.pop(k, None)
        if new_v is None:
            list_of_changes.append(f'  - {k}: {v}')
        elif new_v == v:
            list_of_changes.append(f'    {k}: {v}')
        elif new_v != v:
            list_of_changes.append(f'  - {k}: {v}')
            list_of_changes.append(f'  + {k}: {new_v}')

    for k, v in temp.items():
        list_of_changes.append(f'  + {k}: {v}')

    list_of_changes.append('}')

    return '\n'.join(list_of_changes)
