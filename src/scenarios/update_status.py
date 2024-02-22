from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime

from entities.task import TaskStatus


class WrongStatusCaseException(Exception):
    ...


@dataclass
class UpdateStatusDto:
    task_id: str
    status: TaskStatus
    update_time: datetime

    @classmethod
    def from_request(cls, task_id: str, status: str) -> 'UpdateStatusDto':
        if not TaskStatus.has_value(status):
            raise WrongStatusCaseException('No such value')
        return cls(task_id=task_id, status=TaskStatus[status], update_time=datetime.now())


class IUpdateStatusRepository(metaclass=ABCMeta):

    @abstractmethod
    def update_task(self, task: UpdateStatusDto) -> None: ...


class UpdateStatusInteractor:
    def __init__(self, repository: IUpdateStatusRepository):
        self._repository = repository

    def update_status(self, task_id: str, status: str) -> None:
        return self._repository.update_task(
            task=UpdateStatusDto.from_request(task_id, status),
        )
