import re
from re import Match


class VhdlParser:

    ENTITY_PATTERN = re.compile(r'entity\s+(\w+)\s+is\s*[\s\S]*?end\s+\1\s*;', re.DOTALL)
    GENERIC_PATTERN = re.compile(r'generic\s*\(\s*(.*?)\s*\)\s*;', re.DOTALL)
    PORT_PATTERN = re.compile(r'port\s*\(\s*[\s\S]*?(\s*;\s*\)\s*|\s*\)\s*;)\s*(end\s+\w+\s*;)', re.DOTALL)

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def get_all_nodes_variables(self) -> list[str]:
        return self._change_dict_port_types()

    def _change_dict_port_types(self) -> list[str]:
        port_name_type: dict[str, str] = self._get_port_datatype()
        nodes_name: list[str] = []
        N: int = self._extract_generic_content()

        for node_name, type_and_size in port_name_type.items():
            if type_and_size.startswith('std_logic_vector'):
                vhdl_vector_match = re.match(r'std_logic_vector\(\s*(\S+)\s*(downto|upto)\s*(\S+)\s*\)',
                                             type_and_size)
                first_idx: int = eval(vhdl_vector_match.group(1))
                second_idx: int = eval(vhdl_vector_match.group(3))
                vhdl_vector_range: int = abs(first_idx - second_idx)
                nodes_name.extend(f'{node_name}[{i}]' for i in range(vhdl_vector_range + 1))
            else:
                nodes_name.append(node_name)

        return nodes_name

    def _get_port_datatype(self) -> dict[str, str]:
        port_name_type: dict[str, str] = {}
        port_content: list[tuple] = self._extract_port_content()
        for name, direction, type_and_size in port_content:
            type_and_size: str = re.sub(r'\n\s*\)', '', type_and_size)
            port_name_type[name] = type_and_size
        return port_name_type

    def _extract_port_content(self) -> list[tuple]:
        entity_content: str | None = self._get_entity_content()
        if not entity_content:
            return []

        port_match: Match[str] = self.PORT_PATTERN.search(entity_content)
        if port_match:
            port_content = port_match.group()
            return re.findall(
                r'(\w+)\s*:\s*(in|out)\s*(\S(?:[^;]*\S)?\s*(?:\(\s*\S(?:[^;]*\S)?\s*\))?)\s*;', port_content)
        return []

    def _extract_generic_content(self) -> int:
        entity_content: str | None = self._get_entity_content()
        if not entity_content:
            return -1

        generic_match: Match[str] = self.GENERIC_PATTERN.search(entity_content)
        channel_numbers: int = -1

        if generic_match:
            generic_content: str = generic_match.group(1)
            generic_variables: list[tuple] = re.findall(r'(\w+)\s*:\s*(\w+)\s*:=\s*(\S+)\s*', generic_content)
            for name, _, value in generic_variables:
                if name == 'N':
                    channel_numbers = int(value)

        return channel_numbers

    def _get_entity_content(self) -> str | None:
        vhdl_code: str = self._read_vhdl_file(self.file_path)
        entity_match: Match[str] = self.ENTITY_PATTERN.search(vhdl_code)
        return entity_match.group(0) if entity_match else None

    @staticmethod
    def _read_vhdl_file(file_path: str) -> str:
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise Exception(f"Error reading file: {e}")
