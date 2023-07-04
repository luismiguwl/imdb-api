from main import findJSON
from dataclasses import dataclass


@dataclass
class IMDBApi:
    imdbCode: str

    def search(self) -> dict:
        return findJSON(self.imdbCode)
