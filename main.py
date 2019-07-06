import logging
from PIL import Image
from image_manipulator import ImageManipulator
from utils import add_arguments_to_parse
from utils import configure_logger
from utils import DirectoryNotFoundError


def main():
    images_path = ImageManipulator.get_images_path(args.source)
    for image in images_path:
        image_manipulator = ImageManipulator(image, args.name)
        new_image_path = image_manipulator.create_new_image_path(args.destination)
        with Image.open(image) as img:
            if args.size:
                image_manipulator.resize_image_to_thumbnail(img, args.size)
            if args.jpg:
                img = image_manipulator.convert_to_jpg(img)
            img.save(new_image_path)
            logging.info('Converting finished with success. The new image path is %s', new_image_path)


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
