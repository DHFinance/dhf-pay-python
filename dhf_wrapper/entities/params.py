from dataclasses import dataclass
from typing import List, Optional

from dhf_wrapper.base_dto import BaseDto


@dataclass
class ListParamsDTO(BaseDto):
    fields: Optional[List[str]] = None
    s: Optional[str] = None
    filter: Optional[List[str]] = None
    or_: Optional[List[str]] = None
    sort: Optional[List[str]] = None
    join: Optional[List[str]] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    page: Optional[int] = None
    cache: Optional[int] = None

    def make(cls, data):
        result = super(ListParamsDTO, cls).make(data)
        if '_or' in result:
            result['or'] = result.pop('_or')
        return result
