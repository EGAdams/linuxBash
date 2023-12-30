import os

def write_code_to_directory(directory, file_name, code):
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'w') as file:
        file.write(code)
    return f'Code successfully written to {file_path}'