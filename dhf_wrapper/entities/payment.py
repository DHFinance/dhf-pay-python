from dataclasses import dataclass

from dhf_wrapper.base_dto import BaseDto


@dataclass
class PaymentIdDTO(BaseDto):
    id: int


@dataclass
class PaymentDTO(BaseDto):
    amount: int
    comment: str
