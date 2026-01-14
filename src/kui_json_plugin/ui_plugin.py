from kui.core.app import KamaApplication

from kui_json_plugin.provider.metadata import JsonMetadataProvider
from kui_json_plugin.provider.section import JsonControllerSectionProvider
from kui_json_plugin.provider.style import load_colors, load_fonts, load_dynamic_images
from kui_json_plugin.provider.tr import JsonTextResourceProvider


_application = KamaApplication()

_application.provider.metadata = JsonMetadataProvider()
_application.provider.section = JsonControllerSectionProvider()
_application.translations.set_provider(JsonTextResourceProvider())

load_colors(_application)
load_fonts(_application)
load_dynamic_images(_application)
