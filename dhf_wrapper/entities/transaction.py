from dataclasses import dataclass
from typing import List, Optional

from dhf_wrapper.base_dto import BaseDto
from dhf_wrapper.entities.store import StoreDTO


@dataclass
class TransactionParamsDTO(BaseDto):
    fields: Optional[List[str]] = None
    s: Optional[str] = None
    filter: Optional[List[str]] = None
    _or: Optional[List[str]] = None
    sort: Optional[List[str]] = None
    join: Optional[List[str]] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    page: Optional[int] = None
    cache: Optional[int] = None


@dataclass
class TransactionPaymentDTO(BaseDto):
    id: int
    datetime: str
    amount: str
    status: str
    comment: str
    type: int
    text: str
    store: StoreDTO


@dataclass
class TransactionDTO(BaseDto):
    id: int
    status: str
    email: str
    updated: str
    txHash: str
    sender: str
    amount: str
    payment: TransactionPaymentDTO
