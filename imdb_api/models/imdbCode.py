from dataclasses import dataclass


@dataclass
class IMDBCode:
    code: str
    isValid: bool
