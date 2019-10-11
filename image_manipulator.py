import logging
import os
import csv
import textwrap

from PIL import Image
from PIL import ImageDraw
from PIL import ImageEnhance
from PIL import ImageFont

from utils import DirectoryNotFoundError


class ImageManipulator:
    COUNTER = 1
    LOGO_X_WIDTH = 25
    LOGO_Y_WIDTH = 25
    FONT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cairo\Cairo-Black.ttf')
    FONT_SIZE = 60
    TEXT_HEIGHT = 80
    TEXT_PADDING = 30
    TEXT_WIDTH = 22

    def __init__(self, image_path, img_handler, name=None):
        self.image_path = image_path
        self.image = img_handler
        self.new_img_path = ''

        if name:
            _, file_ext = os.path.splitext(self.image_path)
            self.name = f"{name}-{ImageManipulator.COUNTER}{file_ext}"
        else:
            self.name = os.path.basename(self.image_path)

        ImageManipulator.COUNTER += 1

    @property
    def image_width(self):
        """
        Get current image width
        :return: image width
        """
        image_width, _ = self.image.size
        return image_width

    @property
    def image_height(self):
        """
        Get current image height
        :return: image height
        """
        _, image_height = self.image.size
        return image_height

    def create_new_image_path(self, image_dir=None):
        """
        Crete new path to the image file
        :param image_dir: new directory path
        """
        ImageManipulator.check_if_directory_exists(image_dir)
        image_dir = image_dir
        self.new_img_path = os.path.join(image_dir, self.name)

    def save_image(self):
        """
        Save the image
        """
        self.image.save(self.new_img_path)
        logging.info('Converting finished with success. The new image path is %s', self.new_img_path)

    def resize_image_to_thumbnail(self, size):
        """
        Thumbnail the image
        :param size: new image size
        """
        self.image.thumbnail(size)
        logging.info("Size of a %s has been changed to %s px", self.name, size)

    def convert_to_jpg(self):
        """
        Convert the image to jpg format
        """
        self.image = self.image.convert('RGB')
        logging.info('Image %s has been converted to .jpg', self.name)

    def adjust_contrast(self, factor):
        """
        Change the contrast of the image
        :param factor: factory - from 0.0 to 1.0
        """
        enhancer_object = ImageEnhance.Contrast(self.image)
        logging.info('Contrast of image %s has been changed to %s', self.name, factor)
        self.image = enhancer_object.enhance(factor)

    def adjust_brightness(self, factor):
        """
        Change the brightness of the image
        :param factor: factory - from 0.0 to 1.0
        """
        enhancer_object = ImageEnhance.Brightness(self.image)
        logging.info('Brightness of image %s has been changed to %s', self.name, factor)
        self.image = enhancer_object.enhance(factor)

    def change_image_size(self, size):
        """
        Crop the image to provided size
        :param size: new image size
        """
        target_width, target_height = size

        left = (self.image_width - target_width) / 2
        top = (self.image_height - target_height) / 2
        right = (self.image_width + target_width) / 2
        bottom = (self.image_height + target_height) / 2

        self.image = self.image.crop((left, top, right, bottom))
        logging.info('Size of image %s has been changed to %s, %s', self.name, target_width, target_height)

    def paste_logo(self, logo_path):
        """
        Paste a logo to image bottom left corner
        :param logo_path: path to the logo
        :return:
        """
        with Image.open(logo_path) as logo:
            _, logo_height = logo.size
            self.image.paste(logo, (self.LOGO_X_WIDTH, self.image_height-logo_height+self.LOGO_Y_WIDTH), logo)
        logging.info('Logo has been successfully paste')

    def add_quote(self, quote):
        """
        Add a quote to the image
        :param quote: quote text
        """
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype(self.FONT_PATH, self.FONT_SIZE)

        for line in quote:
            text_width, text_height = draw.textsize(line, font=font)
            draw.text(((self.image_width - text_width) / 2, self.TEXT_HEIGHT), line, font=font)
            self.TEXT_HEIGHT += text_height + self.TEXT_PADDING

        logging.info('Quote: "%s" has been added to image %s', " ".join(quote), self.name)

    @classmethod
    def get_quotes_from_file(cls, csv_path):
        """
        Load quotes from csv file
        :param csv_path: csv file pat
        :return: list of quotes
        """
        quotes_list = []
        with open(csv_path, encoding='windows-1252,', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, quotechar="'", delimiter='\t')
            for row in csv_reader:
                quotes_list.append(textwrap.wrap(row[0], width=cls.TEXT_WIDTH))
        return quotes_list

    @staticmethod
    def get_images_path(image_dir=None):
        """
        Get path for images
        :param image_dir: image directory
        :return: images path
        """
        ImageManipulator.check_if_directory_exists(image_dir)
        image_dir = image_dir

        images = []
        for img_file in os.listdir(image_dir):
            img_path = os.path.join(image_dir, img_file)
            images.append(img_path)

        return images

    @staticmethod
    def check_if_directory_exists(directory):
        """
        Check if directory exists
        :param directory: directory path
        """
        if not os.path.isdir(directory):
            raise DirectoryNotFoundError(f"Provided directory does not exist: {directory}")
