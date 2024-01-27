import logging
import argparse
import directoryChecker
import metadataChecker

def main():
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(
                    prog='python3 main.py',
                    description='This program verifies multiple rules that we want to have enforced on the music library')
    parser.add_argument('music_folder', help='Absolute path to the music folder')
    parser.add_argument('-a', '--all', help="Run all the checks", action='store_true')
    parser.add_argument('--structure', help="Check if the folder structure complies", action='store_true')
    parser.add_argument('--metadata', help="Check if the metadata of the files matches the data stored in the path", action='store_true')

    args = parser.parse_args()

    # handle the arguments
    if args.all or args.structure:
        logging.info("Checking the folder structure")
        directoryChecker.check(args.music_folder)

    if args.all or args.metadata:
        logging.info("Checking the metadata")
        metadataChecker.check(args.music_folder)

if __name__ == '__main__':
    main()
