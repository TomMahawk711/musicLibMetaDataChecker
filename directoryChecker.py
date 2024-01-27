import logging
import os
import re

"""
    This files checks all the files in the directory if the comply to the
    defined naming convention. The naming convention is hardcoded here but
    can be changed if the regex expressions are modified.

    Current convention:
        <artist>/<year>-<album name>/CD<Num>/<track num> - <track name>.<file type>
        <artist>/<year>-<album name>/<track num> - <track name>.<file type>

    Example:
        Alestorm/2011 - Back Through Time/02 - Shipwrecked.mp3
"""

# NAMING CONVENTION CONFIG
ARTIST = r'.+'
ALBUM = r'\d{4} - .+'
DISC = r'CD\d+'
TRACK = r'\d{2} - .+\.(mp3|flac)'
COVER_IMG = r'.+\.(jpg|png)'

IGNORE_COVER_IMG = True

FILES_TO_IGNORE = ['.DS_Store']


def check(absolute_path):
    naming_violation_counter = 0

    for root, _, files in os.walk(absolute_path):
        relative_path = '.' + root[len(absolute_path):]
        naming_violation_counter += _check_directory(relative_path, files)

    logging.info(f'count naming violations: {naming_violation_counter}')


def _check_directory(root, files):
    naming_violation_counter = 0
    for file in files:
        file_path = os.path.join(root, file)

        # ignore those files
        if file in FILES_TO_IGNORE:
            continue

        # quick check
        SEPERATOR = r'(\/|\\)'
        OPTIONAL_DISK = f'({DISC}{SEPERATOR})?'
        if re.match(f'\.{ARTIST}{SEPERATOR}{ALBUM}{SEPERATOR}{OPTIONAL_DISK}{TRACK}', file_path):
            continue

        # ignore cover images (need to lie with the album)
        if IGNORE_COVER_IMG and re.match(f'\.{ARTIST}{SEPERATOR}{ALBUM}{SEPERATOR}{OPTIONAL_DISK}{COVER_IMG}', file_path):
            continue

        # at this point the quick check failed and we hava a invalid file
        logging.warning(f'naming violation at: {file_path}')
        naming_violation_counter += 1
    return naming_violation_counter
