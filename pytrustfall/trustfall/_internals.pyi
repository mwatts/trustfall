from typing import Any, Dict, Iterator, Mapping

from .adapter import Adapter

class AdapterShim:
    def __init__(self, adapter: Adapter[Any]) -> None: ...

class FrontendError(Exception): ...
class InvalidIRQueryError(Exception): ...
class InvalidSchemaError(Exception): ...
class ParseError(Exception): ...
class QueryArgumentsError(Exception): ...
class ValidationError(Exception): ...

class Schema:
    def __init__(self, schema_txt: str) -> None: ...

def interpret_query(
    adapter: AdapterShim, schema: Schema, query: str, arguments: Mapping[str, Any]
) -> Iterator[Dict[str, Any]]: ...