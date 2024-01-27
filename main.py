import logging
import directoryChecker


def main():
    logging.basicConfig(level=logging.INFO)
    directoryChecker.check(r"\\10.69.0.4\music_share")

if __name__ == '__main__':
    main()
