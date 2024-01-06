import logging
import os
import re

ARTIST = r'.+'
ALBUM = r'\d{4} - .+'
DISC = r'CD(\d+)'
TITLE = r'\d{2} - .+\..+'

SINGLE_DISC_ALBUM = fr'^{ARTIST}\/{ALBUM}\/{TITLE}$'
MULTI_DISC_ALBUM = fr'^{ARTIST}\/{ALBUM}\/{DISC}\/{TITLE}$'


def main():
    logging.basicConfig(level=logging.INFO)
    _check_directories()


def _check_directories():
    incorrect_directory_naming_counter = 0

    for root, _, files in os.walk('.'):
        incorrect_directory_naming_counter = check_directory(root, files, incorrect_directory_naming_counter)

    logging.info(f'incorrect instances: {incorrect_directory_naming_counter}')


def check_directory(root, files, incorrect_directory_naming_counter):
    for file in files:
        file_path = os.path.join(root, file)

        if '.DS_Store' in file or not _is_audio_file(file):
            continue

        if not re.match(SINGLE_DISC_ALBUM, file_path):
            incorrect_directory_naming_counter += 1
            logging.warning(f'directory incorrect: {file_path}')

    return incorrect_directory_naming_counter


def _is_audio_file(filename):
    _, file_extension = os.path.splitext(filename)
    return '.mp3' in file_extension or '.flac' in file_extension


if __name__ == '__main__':
    main()
