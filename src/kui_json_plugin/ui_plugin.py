from kui.core.app import KamaApplication

from kui_json_plugin.provider.metadata import JsonMetadataProvider
from kui_json_plugin.provider.section import JsonControllerSectionProvider
from kui_json_plugin.provider.style import load_colors, load_fonts, load_dynamic_resources
from kui_json_plugin.provider.tr import JsonTextResourceProvider


_application = KamaApplication()

_application.metadata_provider = JsonMetadataProvider()
_application.section_provider = JsonControllerSectionProvider()
_application.text_resources.set_provider(JsonTextResourceProvider())

load_colors(_application)
load_fonts(_application)
load_dynamic_resources(_application)
