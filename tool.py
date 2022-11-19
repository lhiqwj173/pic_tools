import os


def apply_all(func, root):
    for path, dir_list, file_list in os.walk(root):
        for file_name in file_list:
            func(os.path.join(path, file_name))
