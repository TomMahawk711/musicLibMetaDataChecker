import logging
import os
import eyed3

VALID_FILE_TYPES = ["mp3"]

#change log level for eyed3 module
logging.getLogger('eyed3.id3.tag').setLevel(logging.ERROR)

def check(absolute_path):
    metadata_violation_counter = 0

    for root, _, files in os.walk(absolute_path):
        relative_path = '.' + root[len(absolute_path):]
        metadata_violation_counter += _check_metadata(relative_path, root, files)

    logging.info(f'count metadata violations: {metadata_violation_counter}')

def _get_data_from_file_path(relative_file_path):
    data = os.path.normpath(relative_file_path).split(os.sep)
    title = ''.join(data[-1][5:].split('.')[:-1])
    album = data[-2][7:]
    track_num = int(data[-1][:2])
    recording_date = data[-2][:4]
    return {"artist" : data[-3], "album" : album, "title" : title, 'track_num': track_num, 'recording_date': recording_date}

def _check_metadata(relative_path, absolute_path, files):
    metadata_violation_counter = 0
    for file in files:
        absolute_file_path = os.path.join(absolute_path, file)
        relative_file_path = os.path.join(relative_path, file)

        # check if the file should be considered
        if any(filter(relative_file_path.endswith, VALID_FILE_TYPES)) == False:
            continue

        path_data = _get_data_from_file_path(relative_file_path)
        audiofile = eyed3.load(absolute_file_path)

        # artist check
        if audiofile.tag.artist != path_data['artist']:
            logging.warning(f'Metadata violation mismatch artist: Expected: {path_data["artist"]} Actual: {audiofile.tag.artist}')
            metadata_violation_counter += 1

        # album check
        if audiofile.tag.album != path_data['album']:
            logging.warning(f'Metadata violation mismatch album: Expected: {path_data["album"]} Actual: {audiofile.tag.album}')
            metadata_violation_counter += 1

    	# recording year check
        if str(audiofile.tag.recording_date) != path_data['recording_date']:
            logging.warning(f'Metadata violation mismatch recording date: Expected: {path_data["recording_date"]} Actual: {audiofile.tag.recording_date}')
            metadata_violation_counter += 1

        # track title check
        if audiofile.tag.title != path_data['title']:
            logging.warning(f'Metadata violation mismatch track title: Expected: {path_data["title"]} Actual: {audiofile.tag.title}')
            metadata_violation_counter += 1

        # track number check
        if audiofile.tag.track_num.count != path_data['track_num']:
            logging.warning(f'Metadata violation mismatch track num: Expected: {path_data["track_num"]} Actual: {audiofile.tag.track_num}')
            metadata_violation_counter += 1

    return metadata_violation_counter


# keep this here for the fixer as information
#audiofile.tag._setDate(b"TYER", "2009")
#audiofile.tag.save()
