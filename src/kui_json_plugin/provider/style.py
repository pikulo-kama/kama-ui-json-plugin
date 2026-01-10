import os.path

from kui.core.app import KamaApplication
from kui.style.type import KamaComposedColor, KamaColor, KamaFont, DynamicResource
from kutil.file import read_file
from kutil.file_type import JSON


def load_colors(application: KamaApplication):

    colors_path = application.discovery.config(JSON.add_extension("colors"))

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
    fonts_path = application.discovery.config(JSON.add_extension("fonts"))

    if not os.path.exists(fonts_path):
        return

    fonts = read_file(fonts_path, as_json=True)

    for font_object in fonts:
        font = KamaFont(**font_object)
        application.style.add_font(font)


def load_dynamic_resources(application: KamaApplication):
    resources_path = application.discovery.config(JSON.add_extension("resources"))

    if not os.path.exists(resources_path):
        return

    resources = read_file(resources_path, as_json=True)

    for resource_object in resources:
        resource = DynamicResource(**resource_object)
        application.style.add_dynamic_resource(resource)
