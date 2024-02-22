from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto


class TaskStatus(Enum):
    in_backlog = auto()
    prioritized = auto()
    in_work = auto()
    in_review = auto()
    done = auto()

    @classmethod
    def has_value(cls, value):
        return value in cls._member_names_


@dataclass
class TaskEntity:
    task_id: str
    description: str
    create_time: datetime
    update_time: datetime
    status: TaskStatus
