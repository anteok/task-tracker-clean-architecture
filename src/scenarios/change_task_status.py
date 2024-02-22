from abc import ABCMeta, abstractmethod

from entities.task import TaskStatus


class IChangeTaskStatusRepository(metaclass=ABCMeta):

    @abstractmethod
    def change_task_status(self, task_id: str, status: str) -> None: ...


class ChangeTaskStatusInteractor:
    def __init__(self, repository: IChangeTaskStatusRepository):
        self._repository = repository

    def change_task_status(self, task_id: str, status: str) -> None:
        return self._repository.change_task_status(task_id, status)
