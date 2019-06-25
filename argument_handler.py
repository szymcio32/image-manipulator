import argparse


class ArgumentHandler:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def add_arguments_to_parse(self):
        self.parser.add_argument('--size', metavar='px', type=int, nargs=2, default=None)
        self.parser.add_argument('--name', metavar="file_name", type=str, default=None)
        self.parser.add_argument('--jpg', action='store_true')
        args = self.parser.parse_args()

        return None if not args.size else tuple(args.size), args.jpg, args.name
