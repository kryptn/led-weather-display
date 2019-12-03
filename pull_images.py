import json

import requests
from PIL import Image
from htmllistparse import htmllistparse

url = "https://radar.weather.gov/ridge/RadarImg/N0R/ICT/"

# url = "https://radar.weather.gov/ridge/RadarImg/N0R/FTG/"

cwd, listings = htmllistparse.fetch_listing(url)

listing_files = [{"url": url + file.name, "listing": file} for file in listings]

manifest = []


def download_new_images():
    for listing in listings:

        m = {
            "filename": f"images/{listing.name}",
            "url": url + listing.name,
            "time_struct": listing.modified,
        }

        img = requests.get(m["url"])

        with open(m["filename"], 'wb') as fd:
            fd.write(img.content)

        try:
            im = Image.open(m["filename"])
        except IOError:
            print("bad image?")
            continue

        manifest.append(m)

    with open("images/manfiest.json", 'w') as fd:
        json.dump(manifest, fd)


if __name__ == '__main__':
    download_new_images()
