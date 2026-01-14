import os

from kui.core.metadata import WidgetMetadata
from kui.core.provider import MetadataProvider
from kui.core.shortcut import resolve_config
from kui.transformer.widget import JSONWidgetDataTransformer
from kutil.file import read_file
from kutil.file_type import JSON


_rename_keys = {
    "id": "widget_id",
    "type": "widget_type",
    "layout": "layout_type",
    "section": "section_id",
    "parent": "parent_widget_id",
    "style_id": "style_object_name",
    "alignment": "alignment_string"
}


class JsonMetadataProvider(MetadataProvider):

    def provide(self, section_id: str) -> list[WidgetMetadata]:

        section_file_name = JSON.add_extension(section_id)
        metadata_file_path = resolve_config("widgets", section_file_name)

        if not os.path.exists(metadata_file_path):
            return []

        transformer = JSONWidgetDataTransformer()
        nested_data = read_file(metadata_file_path, as_json=True)
        widget_data: list[dict] = transformer.flatten(nested_data)
        metadata = []

        for widget in widget_data:

            stylesheet = widget.get("stylesheet", "{}")
            stylesheet = self._parse_stylesheet(stylesheet)

            if stylesheet:
                widget["stylesheet"] = stylesheet

            for key, target_key in _rename_keys.items():
                if key in widget:
                    widget[target_key] = widget.pop(key)

            widget_meta = WidgetMetadata(**widget)
            metadata.append(widget_meta)

        return metadata
