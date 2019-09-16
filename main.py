import logging

from PIL import Image

from image_manipulator import ImageManipulator
from utils import add_arguments_to_parse
from utils import configure_logger
from utils import DirectoryNotFoundError


def main():
    """
    Main function of script
    """
    images_path = ImageManipulator.get_images_path(args.source)
    if args.quotes:
        quotes = ImageManipulator.get_quotes_from_file(args.quotes)
    for index, image in enumerate(images_path):
        with Image.open(image) as img:
            image_manipulator = ImageManipulator(image, img, args.name)
            image_manipulator.create_new_image_path(args.destination)
            if args.thumbnail:
                image_manipulator.resize_image_to_thumbnail(args.thumbnail)
            if args.jpg:
                image_manipulator.convert_to_jpg()
            if args.contrast:
                image_manipulator.adjust_contrast(args.contrast)
            if args.brightness:
                image_manipulator.adjust_brightness(args.brightness)
            if args.crop:
                image_manipulator.change_image_size(args.crop)
            if args.logo:
                image_manipulator.paste_logo(args.logo)
            if args.quotes:
                try:
                    image_manipulator.add_quote(quotes[index])
                except IndexError as exc:
                    logging.error("Number of quotes should be the same as number of images")
            image_manipulator.save_image()


if __name__ == '__main__':
    configure_logger()
    args = add_arguments_to_parse()
    try:
        main()
    except FileNotFoundError as exc:
        logging.error("File not found %s", exc)
    except DirectoryNotFoundError as exc:
        logging.error(exc)
    except Exception as exc:
        logging.error(exc)
