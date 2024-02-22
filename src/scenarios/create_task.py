from abc import ABCMeta, abstractmethod
from datetime import datetime

from entities.task import TaskEntity, TaskStatus


class ICreateTaskRepository(metaclass=ABCMeta):

    @abstractmethod
    def create_task(self, dto: TaskEntity) -> None: ...


class CreateTaskInteractor:

    def __init__(self, repository: ICreateTaskRepository):
        self._repository = repository

    def create_task(self, task_id: str, description: str) -> None:
        self._repository.create_task(TaskEntity(
            task_id=task_id,
            description=description,
            create_time=datetime.now(),
            update_time=datetime.now(),
            status=TaskStatus.in_backlog,
        ))
