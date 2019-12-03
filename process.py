import json

from PIL import Image

from sonar import sonar


def get_pixels_from_line(line, im: Image):
    def _coords(z):
        x = im.width / 2 + round(z.real)
        y = im.height / 2 + round(z.imag)
        return x, y

    return [im.getpixel(_coords(z)) for z in line]


def sonar_scan_image(filename, scan_length, samples):
    im = Image.open(filename)
    rgb_img = im.convert('RGB')

    columns = [get_pixels_from_line(l, rgb_img)[::-1] for l in sonar(scan_length, samples, ticks=600)]

    ni = Image.new('RGB', (len(columns), len(columns[0])), (255, 255, 255))
    ni.putdata([x for y in zip(*columns) for x in y])

    return ni


def sonar_scan_but_just_pixel_data(filename, scan_length, samples):
    im = Image.open(filename)
    rgb_img = im.convert('RGB')

    columns = [get_pixels_from_line(l, rgb_img)[::-1] for l in sonar(scan_length, samples)]

    return columns


def stitch_all_images():
    with open('images/manfiest.json') as fd:
        manifest = json.load(fd)

    images = []
    for item in manifest:
        images.append(sonar_scan_image(item['filename']))

    im = Image.new('RGB', images[0].size)

    im.save('something.gif', append_images=images, save_all=True, duration=100, loop=100)


def do_gif_thing():
    with open('images/manfiest.json') as fd:
        manifest = json.load(fd)

    scan_length = 250
    samples = 250

    images = []
    for item in manifest:
        images.append(sonar_scan_but_just_pixel_data(item['filename'], scan_length, samples))

    swapped = zip(*images)

    built = []
    for columns in swapped:
        rotated = [x for y in zip(*columns) for x in y]
        ni = Image.new('RGB', (len(rotated), rotated[0]), (255, 255, 255))
        ni.putdata()
        built.append(ni)

    im = Image.new('RGB', (len(images), len(images[0])))

    im.save('another.gif', append_images=built, save_all=True, duration=100, loop=100)


if __name__ == '__main__':
    do_gif_thing()
