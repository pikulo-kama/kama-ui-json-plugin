import os

from kui.core.controller import WidgetController
from kui.core.provider import ControllerSectionProvider, Section
from kui.core.shortcut import resolve_data
from kutil.file import read_file
from kutil.file_type import JSON


class JsonControllerSectionProvider(ControllerSectionProvider):

    def provide(self, controller: "WidgetController") -> list[Section]:

        sections = []
        config_file_name = JSON.add_extension(controller.__class__.__name__)
        section_file_path = resolve_data("sections", config_file_name)

        if not os.path.exists(section_file_path):
            return sections

        section_data = read_file(section_file_path, as_json=True)

        for section in section_data:
            section_meta = Section(**section)
            sections.append(section_meta)

        return sections
