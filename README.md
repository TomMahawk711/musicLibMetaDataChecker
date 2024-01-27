# MusicLib Checker & Fixer

## Description

This script can be used to verify that the files in the music library
complie to the defined structure. This script will check (depending on
the arguments) check if the paths are valid and also if the metadata
of the music files match the folder structure. In case of a error a
warning will be printed via the logger.

### Music Lib Structure

Our music library is structured in the following way

- `<artist>/<release_year> - <album>/<track number> - <track-tile>`
- `<artist>/<release_year> - <album>/CD<cd number>/<track number> - <track-tile>`

Example: `Alestorm/2011 - Back Through Time/02 - Shipwrecked.mp3`

Important: The track number is always two chars lonng.

## Usage

```
usage: python3 main.py [-h] [-a] [--structure] [--metadata] music_folder

This program verifies multiple rules that we want to have enforced on the music library

positional arguments:
  music_folder  Absolute path to the music folder

options:
  -h, --help    show this help message and exit
  -a, --all     Run all the checks
  --structure   Check if the folder structure complies
  --metadata    Check if the metadata of the files matches the data stored in the path
```

### Docker

If you for some reason want to use docker to run the script you can do so
with the following commands:

```bash
# PowerShell
docker run -v ${PWD}:/app -v <music_folder>:/music -w /app -it python sh -c "pip install -r requirements.txt && python main.py <arguments> /music"

# Windows CMD
docker run -v %cd%:/app -v <music_folder>:/music -w /app -it python sh -c "pip install -r requirements.txt && python main.py <arguments> /music"

# Linux
docker run -v $(pwd):/app -v <music_folder>:/music -w /app -it python sh -c "pip install -r requirements.txt && python main.py <arguments> /music"
```

Repalce `<music_folder>` with absolute path the music folder that you want to scan. Replace `<arguments>` with the arguments that should be execute.
Do not change anything else.

Info: Your current working directory needs the be the top level folder of the project.

### Requirements

The requirements can be found in the `requirements.txt` file and are also listed here:

```
eyed3==0.9.7
```

If you want to install the requirements via the `requirements.txt` file you can use the command:

```bash
python3 -m pip install -r ./requirements.txt
# or
pip3 install -r ./requirements.txt
```

## Contribute

If you want to contribute to the project you can view the open issues
and fix / implement something from there. If there are no open issues
or nothing that picks your intrest then you can also contact one of
the more active developers.

### Feature request

In case you are missing a feature then you are encouraged to open a
issue describing the feature and why it would be a good idea to
implented it.

### Contributes

- TomMahawk711
- UnHold
