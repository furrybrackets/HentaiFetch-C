#!/usr/bin/python
# This software was written by
# SteveGremory and he wants you to
# switch to an UNIX like operating system.
import utils
import argparse
from term_img.image import TermImage

parser = argparse.ArgumentParser(description='Get hentai right in your terminal.')
parser.add_argument('--tags', help='The tags you want to have for image search.', required=True)
parser.add_argument('--count', help='The number of images to fetch and select a random one form.', required=False)

# Parse the args
args = vars(parser.parse_args())

# Get time image
url = utils.rule34(args["tags"].replace(",", "+"), 100)

# Print to terminal
image = TermImage.from_url(url)
image.draw_image("left")