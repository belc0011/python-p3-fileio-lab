from pathlib import Path
def write_file(file_name, file_content):
    new_file_name=str(file_name)
    with open(new_file_name + '.txt', 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    new_file_name = str(file_name)
    with open(new_file_name + '.txt', 'a') as file:
        file.write(append_content)

def read_file(file_name):
    new_file_name = str(file_name)
    with open(new_file_name + '.txt', 'r') as file:
        file_contents = file.read()
        return file_contents

