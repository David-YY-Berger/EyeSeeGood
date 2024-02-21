class Person:
    def __init__(self, name):
        self.name = name
        self.friend_name_list = []


class Tag:
    def __init__(self, addressee, content):
        self.addressee = addressee
        self.content = content


def find_person_index(persons, target_person_name):
    for i, person in enumerate(persons):
        if person.name == target_person_name:
            return i
    return -1