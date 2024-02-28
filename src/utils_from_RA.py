import os
import shutil



empty_char = '-'

def readable(str):
    return str.capitalize().replace('_', ' ')


def get_input_ensure_valid(prompt, boolean_function, error_msg):
    buf = ''
    while True:
        buf = input(prompt).replace('"',''). replace("'", "")
        if boolean_function(buf):
            return buf
        else:
            print(error_msg)



def get_input_list(prompt):
    print(prompt + ". Enter 'end' to finish")
    input_list = []
    buf = " "
    while buf.lower() != "end":
        input_list.append(buf)
        buf = input()
    input_list = [s for s in input_list if not s.isspace()]
    return input_list


def clear_create_dir(this_dir):
    try:
        shutil.rmtree(this_dir)
    except FileNotFoundError:
        foo = '' # ignore if file not found
    except Exception as e:
        print(f"An error occurred: {e}")
    os.makedirs(this_dir)


def get_input_enum_options(prompt, option_list):
    print(prompt)
    print(" (Enter just the number)")
    possible_options = []
    for op in option_list:
        print(str(op.value) + ". " + readable(op.name))
        possible_options.append(str(op.value))
    keep_going = True
    while keep_going:
        cmd = input()
        if not cmd.isnumeric():
            print("Please enter a number")
        elif cmd not in possible_options:
            print("Please only enter one of the given options")
        else:
            keep_going = False
            return int(cmd)


def write_txt_to_file(path, content, encoding='utf-8'):
    with open(path, 'w', encoding=encoding) as file:
        file.write(content)


def append_txt_to_file(path, content, encoding='utf-8'):
    with open(path, 'a', encoding=encoding) as file:
        file.write(content)


def read_lines_as_list_from_file(path, encoding='utf-8'):
    res = []
    with open(path, 'r', encoding=encoding) as file:
        lines = file.readlines()
    for line in lines:
        res.append(line.strip())
    return res


def read_file_content_as_str(path, encoding='utf-8'):
    try:
        with open(path, 'r', encoding=encoding) as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print(f"The file at {path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")



def simplify_section_header(orig_section_header):
    # res = str(orig_section_header).split('>')[0].strip()
    return orig_section_header.replace('Regression - ', '')


def is_excel_file(file_path):
    if not os.path.exists(file_path):
        return False
    _, file_extension = os.path.splitext(file_path)
    excel_extensions = ['.xls', '.xlsx']
    return file_extension.lower() in excel_extensions


def is_csv_file(file_path):
    if not os.path.exists(file_path):
        return False
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == '.csv'


def get_duplicate_in_str_list(str_list):
    set_copy = set(str_list)
    if len(set_copy) != len(str_list):
        # Initialize a dictionary to store the count of each element
        element_count = {}
        # List to store duplicate elements
        duplicates = []

        # Iterate through the list and count occurrences of each element
        for element in str_list:
            if element in element_count:
                element_count[element] += 1
            else:
                element_count[element] = 1

        # Check for duplicates
        for element, count in element_count.items():
            if count > 1:
                duplicates.append(element)

        return duplicates
    else:
        return None  # No duplicates found



def open_list_as_string(lst, separator=" "):
    res = ""
    for s in lst:
        res += s + separator
    return res