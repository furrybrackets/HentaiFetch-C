import json
import requests
import random
import shutil

# Get the image from rule34, returns the url of the image.
def rule34(tags: str, count: int):
    # Try-Catch for the network request
    try:
        # make the request to rule34 to get the images
        data = requests.get(
            "http://rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&limit=" + str(count) + "&tags=" + tags,
            headers={"User-Agent": "linux:Chromium"})

    except json.JSONDecodeError:
        print("JSON Request failed.")
        return

    # Extract the image URL and return it
    return data.json()[random.randrange(count)]["file_url"]

# Generic helper function to download a given image.
def download_image(url: str, location: str):
    r = requests.get(url, stream=True)

    if r.status_code == 200:
        with open(location, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


