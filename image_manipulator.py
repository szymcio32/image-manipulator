import logging
import os

from PIL import ImageEnhance

from utils import DirectoryNotFoundError


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

    def create_new_image_path(self, image_dir=None):
        ImageManipulator.check_if_directory_exists(image_dir)
        image_dir = image_dir

        new_img_path = os.path.join(image_dir, self.name)
        return new_img_path

    def resize_image_to_thumbnail(self, img, size):
        img.thumbnail(size)
        logging.info("Size of a %s has been changed to %s px", self.name, size)

    def convert_to_jpg(self, img):
        rgb_img = img.convert('RGB')
        logging.info('Image %s has been converted to .jpg', self.name)
        return rgb_img

    def adjust_contrast(self, img, factor):
        enhancer_object = ImageEnhance.Contrast(img)
        logging.info('Contrast of image %s has been changed to %s', self.name, factor)
        return enhancer_object.enhance(factor)

    @staticmethod
    def get_images_path(image_dir=None):
        ImageManipulator.check_if_directory_exists(image_dir)
        image_dir = image_dir

        images = []
        for img_file in os.listdir(image_dir):
            img_path = os.path.join(image_dir, img_file)
            images.append(img_path)

        return images

    @staticmethod
    def check_if_directory_exists(directory):
        if not os.path.isdir(directory):
            raise DirectoryNotFoundError(f"Provided directory does not exist: {directory}")
