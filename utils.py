import argparse
import logging
import os


class DirectoryNotFoundError(Exception):
    pass


class FactoryRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return (self.start <= other) and (self.end >= other)

    def __repr__(self):
        return f'{self.start} to {self.end}'


def add_arguments_to_parse():
    images_source_dir = os.path.join(os.getcwd(), "images")
    images_destination_dir = os.path.join(os.getcwd(), "changed-images")

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
                        metavar="image_source_directory",
                        type=str,
                        default=images_source_dir,
                        help="Absolute path to image source directory")
    parser.add_argument('--destination',
                        metavar="image_destination_directory",
                        type=str,
                        default=images_destination_dir,
                        help="Absolute path to image destination directory")
    parser.add_argument('--contrast',
                        metavar="contrast_factor",
                        type=float,
                        choices=[FactoryRange(0.0, 1.0)],
                        default=None,
                        help="Factor from 0.0 to 1.0 for image contrast")

    return parser.parse_args()


def configure_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
