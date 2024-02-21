import re

import class_person as cp
import enums
import utils_from_RA as utils
import os

output_q_files_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'EyeSeeGood', 'output_questions')
output_a_files_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'EyeSeeGood', 'output_answers')


def main():
    input(f'erasing directories:\n{output_q_files_dir}\n{output_a_files_dir}\nOk?')
    utils.clear_create_dir(output_q_files_dir)
    utils.clear_create_dir(output_a_files_dir)
    # cmd = utils.get_input_enum_options("What would you like to do?", list(enums.Options))
    # if cmd == enums.Options.CREATE_QUESTION_FILES.value:
    #     create_question_files()
    #     print('question files in: ' + output_dir)
    # elif cmd == enums.Options.READ_ANSWER_FILES.value:
    #     f = ''
    # create_question_files()
    create_answer_files()


def create_answer_files():
    # (1) Get all tags:
    # input_dir = utils.get_input_ensure_valid("Enter the directory that contains the completed question files (absolute path):",
    #                                          os.path.isdir, "please enter a proper directory path!")
    input_dir_path = r"C:\Users\davidbe\Downloads\output_questions"
    all_tag_list = []
    for filename in os.listdir(input_dir_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_dir_path, filename)
            all_tag_list += get_tag_list_from_file(file_path)
#     (2) Write to answer files:
    write_answer_files(tags=all_tag_list)

def get_tag_list_from_file(file_path):

    tag_list = []
    regex_pattern = r'<([^>]*)>([^<]*)</\1>'
    file_content = utils.read_file_content_as_str(file_path)
    # Find all matches using regex
    matches = re.findall(regex_pattern, file_content)
    for match in matches:
        addressee_name, content_of_tag = match
        if content_of_tag.strip() != utils.empty_char:
            tag_list.append(cp.Tag(addressee_name, content_of_tag))
    return tag_list



def write_answer_files(tags):
    # Create a dictionary to store content for each addressee
    addressee_content = {}

    # Iterate over the tags and collect content for each addressee
    for tag in tags:
        addressee = tag.addressee
        content = tag.content

        if addressee not in addressee_content:
            addressee_content[addressee] = []

        # Append content to the addressee's list
        addressee_content[addressee].append(content)

    # Write content to separate files for each addressee
    for addressee, content_list in addressee_content.items():
        # Create a file for each addressee
        file_path = os.path.join(output_a_files_dir, f"answers_{addressee}.txt")
        with open(file_path, 'a') as file:
            # Write content to the file, separating by '\n--\n'
            for content in content_list:
                file.write(content + "\n--\n")


def create_question_files():
    q_list = ['Question 1', 'Question 2', 'Question 3']
    p_list = get_persons()
    for p in p_list:
        p_path = os.path.join(output_q_files_dir, p.name + '_questions.txt')
        utils.write_txt_to_file(p_path, p.name + ', please fill this out:\n\n')
        for i, f in enumerate(p.friend_name_list):
            content = utils.empty_char
            if i <= 2:
                content = '\t(Answer here for ' + q_list[i] + ':)\n'
            elif i ==3:
                utils.append_txt_to_file(p_path, '\n\n\n----------\nBonus Round\n----------')
            utils.append_txt_to_file(p_path, get_full_tag_w_content(f, content))


def get_persons():
    person_names = ['David', 'Ilan', 'Ela', 'Evyatar', 'Shahar', 'lior', 'inga', 'irina', 'roni']
    # must check: 1 no person name is same name
    # 2 numpersons is bigger than list of q's
    persons = [cp.Person(name) for name in person_names]

    # new_p_list = []
    n = len(persons)
    for p in persons:
        # new_p = cp.Person(p.name)
        this_p_index = cp.find_person_index(persons, p.name)
        p.friend_name_list.append(persons[(this_p_index - 1) % n].name)
        for i in range(len(persons)):
            p.friend_name_list.append(persons[(this_p_index + 1 + i) % n].name)
    return persons


def get_beg_tag(person_name):
    return '<' + person_name + '>'


def get_end_tag(person_name):
    return '</' + person_name + '>'


def get_full_tag_w_content(person_name, content):
    return '\n\n' + get_beg_tag(person_name) + '\n' + content + '\n' + get_end_tag(person_name) + '\n\n'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
