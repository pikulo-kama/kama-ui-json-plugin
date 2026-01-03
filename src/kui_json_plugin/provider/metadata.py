import os

from kui.core.metadata import WidgetMetadata
from kui.core.provider import MetadataProvider
from kui.core.shortcut import resolve_config
from kutil.file import read_file
from kutil.file_type import JSON


class JsonMetadataProvider(MetadataProvider):

    def provide(self, section_id: str) -> list[WidgetMetadata]:

        metadata = []
        section_file_name = JSON.add_extension(section_id)
        metadata_file_path = resolve_config("widgets", section_file_name)

        if not os.path.exists(metadata_file_path):
            return metadata

        metadata_json = read_file(metadata_file_path, as_json=True)

        for widget in metadata_json:
            widget_meta = WidgetMetadata(**widget)
            metadata.append(widget_meta)

        return metadata
