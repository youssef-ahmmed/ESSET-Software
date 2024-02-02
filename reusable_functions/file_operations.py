
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
