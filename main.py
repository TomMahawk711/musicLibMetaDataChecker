import logging
import os
import re

REGEX = r'^.+\/\d{4} - .+\/\d{2} - .+\..+$'


def main():
    logging.basicConfig(level=logging.INFO)
    _check_music_library()


def _check_music_library():
    for root, dirs, files in os.walk('.'):
        for file in files:
            file_path = os.path.join(root, file)

            if '.DS_Store' in file or _check_file_extension(file):
                continue

            if not re.match(REGEX, file_path):
                logging.warning(f'FAIL: directory is not correct for -> {file_path}')


def _check_file_extension(filename):
    _, file_extension = os.path.splitext(filename)
    return '.mp3' not in file_extension and '.flac' not in file_extension


if __name__ == '__main__':
    main()
