import logging
import os
from PIL import Image
from argument_handler import ArgumentHandler


IMAGES_DIR = os.path.join(os.getcwd(), "images")
CHANGED_IMAGES_DIR = os.path.join(os.getcwd(), "changed-images")


class ImageManipulator:
    COUNTER = 1

    def __init__(self, image_path, name=None):
        self.image_path = image_path
        if name:
            _, file_ext = os.path.splitext(self.image_path)
            self.name = f"{name}-{ImageManipulator.COUNTER}{file_ext}"
        else:
            self.name = os.path.basename(self.image_path)
        ImageManipulator.COUNTER += 1

    def create_new_image_path(self):
        new_img_path = os.path.join(CHANGED_IMAGES_DIR, self.name)
        return new_img_path

    def resize_image_thumbnail(self, img, size):
        img.thumbnail(size)
        logging.info("Size of a %s has been changed to %s px", self.name, size)

    def convert_to_jpg(self, img):
        rgb_img = img.convert('RGB')
        logging.info('Image %s has been converted to .jpg', self.name)
        return rgb_img

    @staticmethod
    def get_images():
        images = []
        for img_file in os.listdir(IMAGES_DIR):
            img_path = os.path.join(IMAGES_DIR, img_file)
            images.append(img_path)

        return images


if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    argument_handler = ArgumentHandler()
    argument_handler.add_arguments_to_parse()
    args = argument_handler.parser.parse_args()

    images_path = ImageManipulator.get_images()
    for image in images_path:
        image_manipulator = ImageManipulator(image, args.name)
        new_image_path = image_manipulator.create_new_image_path()
        with Image.open(image) as img:
            if args.size:
                image_manipulator.resize_image_thumbnail(img, args.size)
            if args.jpg:
                img = image_manipulator.convert_to_jpg(img)
            img.save(new_image_path)
            logging.info('Converting finished with success. The new image path is %s', new_image_path)