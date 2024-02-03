from .os_operations import dir_list, join_paths, check_is_file, remove_file


def read_text_file(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading file: {e}")


def write_to_text_file(file_path: str, file_content: str) -> None:
    try:
        with open(file_path, 'w') as file:
            file.write(file_content)
    except Exception as e:
        print(f"Error writing content to {file_path}: {str(e)}")


def read_binary_file(file_path: str) -> bytes:
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading file: {e}")


def delete_files(project_path, extension):

    for file_name in dir_list(project_path):
        file_path = join_paths(project_path, file_name)
        if check_is_file(file_path) and file_name.endswith(extension):
            try:
                remove_file(file_path)
            except Exception as e:
                print(f"Error deleting file {file_path}: {str(e)}")
