from dataclasses import asdict, dataclass
from typing import Any

@dataclass
class Task:
    id: int
    title: str
    status: str = "in-progress"
    
    def to_dict(self) -> dict:
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Task":
        return cls(
            id=data["id"],
            title=data["title"],
            status=data["status"]
        )
        
    def __repr__(self) -> str:
        repr_text = (
            f"ID: {self.id}\n"
            f"Title: {self.title}\n"
            f"Status: {self.status}"
        )
        return repr_text