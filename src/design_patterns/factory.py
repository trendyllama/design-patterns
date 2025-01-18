"""

The factory is a creational design pattern we can use to create concrete implementations of an interface.

This pattern is useful for eliminating complex conditional statements when creating objects.
It allows us to create objects without specifying the exact class of object that will be created.
"""

from typing import Protocol
import json
# import xml.etree
# import xml.etree.ElementTree
# import yaml
# import xml


class File(Protocol):
    def read(self) -> str:
        """
        generic read method
        """

    def write(self, data: str) -> None:
        """
        generic write method
        """


class FileParserFactory:
    """
    implement methods for each file type

    these methods will be used to parse the file behind
    a generic parse method

    """

    def _parse_json(self, file: File) -> str:
        with open(file.read(), "r", encoding="utf-8") as f:
            data = json.load(f)

        return data

    def _parse_xml(self, file: File) -> str:
        pass

        # with open(file.read(), 'r', encoding='utf-8') as f:
        #     data = xml.etree.ElementTree.fromstring(f)

        # return data

    def _parse_yaml(self, file: File) -> str:
        pass

        # with open(file.read(), 'r', encoding='utf-8') as f:
        #     data = yaml.load(f)

        # return data

    def parse(self, file: File, file_type: str) -> str:
        """
        generic parse method that can be extended to support other file types

        hides these if statements from behind a clean interface
        """
        if file_type == "json":
            return self._parse_json(file)

        if file_type == "xml":
            return self._parse_xml(file)

        if file_type == "yaml":
            return self._parse_yaml(file)

        raise ValueError(f"Unsupported file type: {file_type}")
