import logging
import os
import re

ARTIST = r'.+'
ALBUM = r'\d{4} - .+'
DISC = r'CD(\d+)'
TRACK = r'\d{2} - .+\..+'


def main():
    logging.basicConfig(level=logging.INFO)
    _check_directories()


def _check_directories():
    incorrect_naming_counter = 0

    for root, _, files in os.walk('.'):
        incorrect_naming_counter += _check_directory(root, files)

    logging.info(f'incorrect directories: {incorrect_naming_counter}')


def _check_directory(root, files):
    incorrect_naming_counter = 0

    for file in files:
        file_path = os.path.join(root, file)

        if '.DS_Store' in file or not _is_audio_file(file):
            continue

        attributes = file_path.split(os.sep)[1:]

        if not _is_matching_single_disc_album(attributes) and not _is_matching_multi_disc_album(attributes):
            incorrect_naming_counter += 1
            logging.warning(f'directory incorrect: {file_path}')

    return incorrect_naming_counter


def _is_audio_file(filename):
    _, file_extension = os.path.splitext(filename)
    return '.mp3' in file_extension or '.flac' in file_extension


def _is_matching_single_disc_album(attributes):
    return (len(attributes) == 3
            and re.match(ARTIST, attributes[0])
            and re.match(ALBUM, attributes[1])
            and re.match(TRACK, attributes[2]))


def _is_matching_multi_disc_album(attributes):
    return (len(attributes) == 4
            and re.match(ARTIST, attributes[0])
            and re.match(ALBUM, attributes[1])
            and re.match(DISC, attributes[2])
            and re.match(TRACK, attributes[3]))


if __name__ == '__main__':
    main()
