# This software was written by
# SteveGremory and he wants you to
# switch to linux.
import requests
import json
import random
import ascii_magic
import argparse

def rule34(tags):
    try:
        data = requests.get(
            "http://rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&limit={}&tags=" + tags,
            headers={"User-Agent": "linux:nooneasked"})
    except json.JSONDecodeError:
        print("Bruh this shit broke.")
        return
    count = len(data.text)
    if count == 0:
        print("Nope, nothing.")
        return
    image_count = 100

    image_url = data.json()[random.randrange(image_count)]["file_url"]
    da_shit = ascii_magic.from_url(image_url)
    ascii_magic.init_terminal()
    ascii_magic.to_terminal(da_shit)

parser = argparse.ArgumentParser(description='Get hentai right in your terminal.')

parser.add_argument('--tag', help='Get hentai right inside your terminal!', required=True)

args = vars(parser.parse_args())
rule34(args['tag'])