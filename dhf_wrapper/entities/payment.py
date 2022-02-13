from dataclasses import dataclass

from dhf_wrapper.base_dto import BaseDto


@dataclass
class PaymentIdDTO(BaseDto):
    id: int


@dataclass
class PaymentDTO(BaseDto):
    store: int
    amount: int
    status: str
    comment: str
    type: int
    text: str
