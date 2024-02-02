import os


def split_pathname(path) -> str:
    return os.path.splitext(path)[0]


def join_paths(path, *paths) -> str:
    return os.path.join(path, *paths)


def dir_list(path) -> list[str]:
    return os.listdir(path)


def check_is_file(path) -> bool:
    return os.path.isfile(path)


def change_dir(path) -> None:
    os.chdir(path)


def get_environ_path() -> str:
    return os.environ.get('PATH')


def change_file_mode(path, mode) -> None:
    os.chmod(path, mode)


def get_directory_name(path) -> str:
    return os.path.dirname(path)


def get_path_separation() -> str:
    return os.pathsep


def get_last_modification_time(path) -> float:
    return os.path.getmtime(path)


def get_basename(path) -> str:
    return os.path.basename(path)
