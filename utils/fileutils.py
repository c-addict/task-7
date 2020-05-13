import os


def search_files(pattern: str, dirs=None) -> set:
    """
    Returns a list of files whose names match the pattern parameter.
    :param pattern:
    :param dirs:
    :return set:
    """
    if dirs is None:
        dirs = ['/']

    found_files = set()
    for path in dirs:
        for root, directory, files in os.walk(path):
            if pattern in files:
                found_files.add((pattern, os.path.join(root, pattern)))
    return found_files

