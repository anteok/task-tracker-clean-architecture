from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, asdict
from datetime import datetime

from entities.task import TaskEntity, TaskStatus


@dataclass
class CreateTaskDto:
    task_id: str
    description: str
    create_time: datetime
    update_time: datetime
    status: str

    @classmethod
    def from_entity(cls, entity: TaskEntity) -> 'CreateTaskDto':
        raw_data = asdict(entity)
        raw_data['status'] = raw_data['status'].name
        return cls(**raw_data)


class CreateTaskInterface(metaclass=ABCMeta):

    @abstractmethod
    def create_task(self, dto: CreateTaskDto) -> None: ...


class CreateTaskInteractor:

    def __init__(self, repository: CreateTaskInterface):
        self._repository = repository

    def create_task(self, task_id: str, description: str) -> None:
        entity = TaskEntity(
            task_id=task_id,
            description=description,
            create_time=datetime.now(),
            update_time=datetime.now(),
            status=TaskStatus.in_backlog,
        )
        self._repository.create_task(CreateTaskDto.from_entity(entity))
