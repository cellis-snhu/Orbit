from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class Task(db.Model):
    __tablename__ = "tasks"

    _id: so.Mapped[int] = so.mapped_column("id", sa.Integer, primary_key=True, autoincrement=True)
    _name: so.Mapped[str] = so.mapped_column("name", sa.String(20), nullable=False)
    _description: so.Mapped[str] = so.mapped_column("description", sa.String(50), nullable=False)
    _priority: so.Mapped[Optional[str]] = so.mapped_column("priority", sa.String(10), nullable=True)
    _completed: so.Mapped[bool] = so.mapped_column("completed", sa.Boolean, default=False, nullable=False)

    def __init__(self, name: str, description: str, priority: Optional[str] = None, completed: bool = False):
        # use property setters to enforce validation
        self.name = name
        self.description = description
        self.priority = priority
        self.completed = completed

    def __repr__(self):
        return (
            f"Task: {self.id} Name: {self.name} Description: {self.description} Priority: {self.priority} Completed: {self.completed}")

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if value is None or len(value) > 20:
            raise ValueError("Invalid task name: must be non-null and <= 20 characters long.")
        self._name = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        if value is None or len(value) > 50:
            raise ValueError("Invalid description: must be non-null and <= 50 characters long.")
        self._description = value

    @property
    def completed(self) -> bool:
        return self._completed

    @completed.setter
    def completed(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("Completed must be a boolean value.")
        self._completed = value

    @property
    def priority(self) -> Optional[str]:
        return self._priority

    @priority.setter
    def priority(self, value: Optional[str]):
        valid_priorities = {"low", "medium", "high"}
        if value is not None and value not in valid_priorities:
            raise ValueError(f"Priority must be one of {valid_priorities} or None.")
        self._priority = value

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
        }
