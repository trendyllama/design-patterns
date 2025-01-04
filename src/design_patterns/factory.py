'''

The factory is a creational design pattern we can use to create concrete implementations of an interface.

This pattern is useful for eliminating complex conditional statements when creating objects.
It allows us to create objects without specifying the exact class of object that will be created.
'''

from typing import Protocol

class File(Protocol):
    def read(self) -> str: ...

    def write(self, data: str) -> None: ...


class FileParser:

    def _parse_json(self, file: File) -> str: ...

    def _parse_xml(self, file: File) -> str: ...

    def parse_yaml(self, file: File) -> str: ...

    def parse(self, file: File, file_type: str) -> str:

        if file_type == 'json':
            return self._parse_json(file)
        elif file_type == 'xml':
            return self._parse_xml(file)
        elif file_type == 'yaml':
            return self.parse_yaml(file)
        else:
            raise ValueError(f'Unsupported file type: {file_type}')


