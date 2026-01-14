import os.path

from kui.core.app import KamaApplication
from kui.style.type import KamaComposedColor, KamaColor, KamaFont, DynamicImage
from kutil.file import read_file
from kutil.file_type import JSON


def load_colors(application: KamaApplication):

    colors_path = application.discovery.data(JSON.add_extension("colors"))

    if not os.path.exists(colors_path):
        return

    colors: list[dict[str, str]] = read_file(colors_path, as_json=True)

    for color_object in colors:
        color = KamaComposedColor(
            color_code=color_object.get("color_code"),
            light_color=KamaColor(color_object.get("light")),
            dark_color=KamaColor(color_object.get("dark"))
        )
        application.style.add_color(color)


def load_fonts(application: KamaApplication):
    fonts_path = application.discovery.data(JSON.add_extension("fonts"))

    if not os.path.exists(fonts_path):
        return

    fonts = read_file(fonts_path, as_json=True)

    for font_object in fonts:
        font = KamaFont(**font_object)
        application.style.add_font(font)


def load_dynamic_images(application: KamaApplication):
    images_path = application.discovery.data(JSON.add_extension("images"))

    if not os.path.exists(images_path):
        return

    images = read_file(images_path, as_json=True)

    for image_object in images:
        image = DynamicImage(**image_object)
        application.style.add_dynamic_image(image)
