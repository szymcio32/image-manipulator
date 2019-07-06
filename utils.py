import argparse
import logging


class DirectoryNotFoundError(Exception):
    pass


def add_arguments_to_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--size',
                        metavar='px',
                        type=int,
                        nargs=2,
                        default=None,
                        help="New size of the image")
    parser.add_argument('--name',
                        metavar="file_name",
                        type=str,
                        default=None,
                        help="New name of the image")
    parser.add_argument('--jpg',
                        action='store_true',
                        help="Convert image to jpg")
    parser.add_argument('--source',
                        metavar="image_source_dir",
                        type=str,
                        default=None,
                        help="Absolute path to image source directory")
    parser.add_argument('--destination',
                        metavar="image_destination_dir",
                        type=str,
                        default=None,
                        help="Absolute path to image destination directory")

    return parser.parse_args()


def configure_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
