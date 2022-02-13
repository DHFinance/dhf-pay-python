from dataclasses import dataclass

from dhf_wrapper.base_dto import BaseDto


@dataclass
class StoreDTO(BaseDto):
    id: int
    url: str
    name: str
    wallet: str
    description: str
    apiKey: str
    blocked: bool
