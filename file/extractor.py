from file.file_processing import file_to_list


def extract_content(files_path):
    files = file_to_list(files_path)
    content = files[0][88:-10], files[1][88:-10]
    return content


def extract_mods():
    return None
