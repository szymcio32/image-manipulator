import logging
import os


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

    def resize_image_to_thumbnail(self, img, size):
        img.thumbnail(size)
        logging.info("Size of a %s has been changed to %s px", self.name, size)

    def convert_to_jpg(self, img):
        rgb_img = img.convert('RGB')
        logging.info('Image %s has been converted to .jpg', self.name)
        return rgb_img

    @staticmethod
    def get_images(image_dir=None):
        images = []
        image_dir = image_dir
        if image_dir is None:
            image_dir = IMAGES_DIR

        for img_file in os.listdir(image_dir):
            img_path = os.path.join(image_dir, img_file)
            images.append(img_path)

        return images
